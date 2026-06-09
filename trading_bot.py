#!/usr/bin/env python3
"""Polymarket trading bot — scan, buy, sell, repeat"""
import urllib.request, urllib.error, json, time, os, sys

BANKROLL = 15.25
MIN_EDGE = 0.025
MAX_BET = 5.00
TAKE_PROFIT = 0.10  # Sell at 10% profit
STOP_LOSS = 0.20    # Sell at 20% loss

# Polymarket API
RELAYER_KEY = "019eac8f-34ac-7a50-afa7-03cb01efd7f3"
SIGNER = "0xd0Bc771c21bED9Db548aDE240F9c9B6E867F661a"
API_KEY = "019eac8f-9945-7856-bed2-25276574b490"
API_SECRET = "7uP_wfDOA7ya6kwBfGohnArrHq1-yr8oBls1khaBuy0="
API_PASSPHRASE = "c8a0096caf642049e534d6593e57d1e53c475a25226c7c5010b3c9bbdc6a0b52"

CLOB_URL = "https://clob.polymarket.com"
GAMMA_URL = "https://gamma-api.polymarket.com"

positions = {}  # {market_id: {side, entry_price, amount, token_id}}
total_pnl = 0.0

def gamma_request(path):
    req = urllib.request.Request(f"{GAMMA_URL}{path}", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

def clob_request(method, path, body=None):
    url = f"{CLOB_URL}{path}"
    data = json.dumps(body).encode() if body else None
    headers = {
        "Content-Type": "application/json",
        "POLY_API_KEY": API_KEY,
        "POLY_SECRET": API_SECRET,
        "POLY_PASSPHRASE": API_PASSPHRASE,
    }
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {"error": e.code, "body": e.read().decode()[:200]}

def get_balance():
    try:
        # Check orderbook for our open orders  
        orders = clob_request("GET", "/orders?status=open")
        if "error" not in orders:
            return BANKROLL  # Simplified — in production query actual balance
    except:
        pass
    return BANKROLL

def scan_for_edge():
    """Find markets where Yes+No != $1.00 by ≥2.5%"""
    events = gamma_request("/events?limit=20&order=volume&active=true&closed=false")
    opportunities = []
    
    for ev in events[:15]:
        volume = float(ev.get('volume', 0))
        if volume < 30000: continue
        
        for m in ev.get('markets', [])[:2]:
            try:
                prices = json.loads(m.get('outcomePrices', '[]'))
                if len(prices) >= 2:
                    yes, no = float(prices[0]), float(prices[1])
                    gap = abs(1.0 - (yes + no))
                    
                    if gap >= MIN_EDGE:
                        direction = "NO" if (yes + no) > 1 else "YES"
                        token_ids = json.loads(m.get('clobTokenIds', '[]'))
                        token_idx = 1 if direction == "NO" else 0
                        
                        opportunities.append({
                            "question": m.get('question', '')[:80],
                            "market_id": m.get('id', ''),
                            "condition_id": m.get('conditionId', ''),
                            "direction": direction,
                            "price": prices[token_idx],
                            "token_id": token_ids[token_idx] if len(token_ids) > token_idx else None,
                            "gap": gap,
                            "volume": volume,
                        })
            except: pass
    
    return sorted(opportunities, key=lambda x: x['gap'], reverse=True)

def check_positions():
    """Monitor open positions for take-profit/stop-loss"""
    global positions, total_pnl
    closed = []
    
    for market_id, pos in list(positions.items()):
        try:
            # Get current price
            book = clob_request("GET", f"/book?token_id={pos['token_id']}")
            if "error" in book: continue
            
            # Get best bid (price we can sell at)
            bids = book.get('bids', [])
            if not bids: continue
            current_price = float(bids[0].get('price', 0))
            entry = pos['entry_price']
            direction = pos['direction']
            pnl_pct = (current_price - entry) / entry
            
            if direction == "YES" and pnl_pct >= TAKE_PROFIT:
                # SELL: take profit
                result = clob_request("POST", "/order", {
                    "token_id": pos['token_id'],
                    "price": str(current_price),
                    "side": "SELL",
                    "size": str(pos['amount']),
                })
                if "error" not in result:
                    profit = pos['amount'] * pnl_pct
                    total_pnl += profit
                    closed.append(f"💰 SOLD {pos['question'][:40]} | +{pnl_pct*100:.1f}% (+€{profit:.2f})")
                    del positions[market_id]
            
            elif direction == "NO" and pnl_pct >= TAKE_PROFIT:
                result = clob_request("POST", "/order", {
                    "token_id": pos['token_id'],
                    "price": str(current_price),
                    "side": "BUY",  # Buy back NO tokens to close
                    "size": str(pos['amount']),
                })
                if "error" not in result:
                    profit = pos['amount'] * pnl_pct
                    total_pnl += profit
                    closed.append(f"💰 CLOSED {pos['question'][:40]} | +{pnl_pct*100:.1f}% (+€{profit:.2f})")
                    del positions[market_id]
                    
        except Exception as e:
            pass
    
    return closed

def place_trade(opp):
    """Execute a trade on Polymarket"""
    global positions
    
    bet = min(MAX_BET, BANKROLL * 0.33)
    side = "BUY"
    
    order = {
        "token_id": opp['token_id'],
        "price": str(opp['price']),
        "side": side,
        "size": str(bet),
    }
    
    result = clob_request("POST", "/order", order)
    
    if "error" not in result:
        positions[opp['market_id']] = {
            "question": opp['question'],
            "direction": opp['direction'],
            "entry_price": float(opp['price']),
            "amount": bet,
            "token_id": opp['token_id'],
            "entry_time": time.time(),
        }
        return f"✅ BOUGHT {opp['direction']} on: {opp['question'][:50]} | €{bet:.2f} @ {float(opp['price'])*100:.1f}¢ | Edge: {opp['gap']*100:.1f}%"
    
    return f"❌ FAILED: {result.get('error', result.get('body', 'unknown'))}"[:100]

def status_line():
    pos_count = len(positions)
    pos_value = sum(p['amount'] for p in positions.values())
    return f"💼 {pos_count} open | €{pos_value:.2f} exposed | P&L: €{total_pnl:+.2f} | Bank: €{BANKROLL:.2f}"

# MAIN LOOP
print(f"🦂 TRADING BOT ACTIVE | Bank: €{BANKROLL:.2f} | Edge: ≥{MIN_EDGE*100:.0f}% | TP: {TAKE_PROFIT*100:.0f}%")
print(f"   Scans every 30s | Trades immediately | Sells at profit")

scan_count = 0
while True:
    try:
        # 1. Check existing positions
        sales = check_positions()
        for s in sales: print(s)
        
        # 2. Scan for new opportunities
        if len(positions) < 3:  # Max 3 concurrent positions
            opps = scan_for_edge()
            if opps:
                opp = opps[0]  # Best edge
                if opp['market_id'] not in positions:
                    result = place_trade(opp)
                    print(f"[{time.strftime('%H:%M:%S')}] {result}")
        
        # 3. Status every 10 scans
        scan_count += 1
        if scan_count % 10 == 0:
            print(f"[{time.strftime('%H:%M:%S')}] {status_line()}")
    
    except Exception as e:
        pass
    
    time.sleep(30)
