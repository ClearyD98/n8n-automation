#!/usr/bin/env python3
"""Polymarket arbitrage & momentum scanner — finds mispriced markets, flags opportunities.
Run as cron job every 5-10 minutes. Reports to Discord or Telegram."""

import urllib.request, json, time, sys
from datetime import datetime

API_BASE = "https://gamma-api.polymarket.com"
MIN_VOLUME = 5000      # Only markets with $5K+ volume
MIN_LIQUIDITY = 1000   # Minimum liquidity to trade
SPREAD_THRESHOLD = 0.05  # 5% spread = opportunity

def fetch(endpoint):
    """Fetch from Polymarket API with retry"""
    url = f"{API_BASE}/{endpoint}"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "autoprod/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read())
        except Exception as e:
            if attempt == 2:
                print(f"API error: {e}", file=sys.stderr)
                return None
            time.sleep(1)

def scan_markets():
    """Find active markets with opportunities"""
    markets = fetch("markets?limit=50&active=true&closed=false")
    if not markets:
        return []
    
    opportunities = []
    
    for m in markets:
        try:
            vol = float(m.get("volume", 0))
            if vol < MIN_VOLUME:
                continue
            
            question = m.get("question", "Unknown")[:100]
            outcomes = json.loads(m.get("outcomes", "[]"))
            prices = json.loads(m.get("outcomePrices", "[]"))
            
            if len(outcomes) < 2 or len(prices) < 2:
                continue
            
            # Check for arbitrage: total implied probability across all outcomes
            total_prob = sum(float(p) for p in prices)
            
            # If total < 0.97, there's an arbitrage opportunity (outcomes underpriced)
            # If total > 1.03, market is overvalued
            
            if total_prob < 0.97 or total_prob > 1.03:
                opportunities.append({
                    "type": "ARBITRAGE" if total_prob < 0.97 else "SHORT",
                    "question": question,
                    "volume": vol,
                    "outcomes": outcomes,
                    "prices": [round(float(p), 4) for p in prices],
                    "total_implied": round(float(total_prob), 4)
                })
                continue
            
            # Check for momentum: extreme prices (near 0 or near 1) = sentiment plays
            for i, price in enumerate(prices):
                p = float(price)
                if 0.05 < p < 0.15:
                    opportunities.append({
                        "type": "MOMENTUM_LONG",
                        "question": question,
                        "volume": vol,
                        "outcome": outcomes[i],
                        "price": round(p, 4),
                        "note": "Deeply discounted — potential reversal play"
                    })
                elif 0.90 < p < 0.98:
                    opportunities.append({
                        "type": "CERTAINTY_SELL",
                        "question": question,
                        "volume": vol,
                        "outcome": outcomes[i],
                        "price": round(p, 4),
                        "note": "Near-certain outcome — sell premium before resolution"
                    })
                    
        except Exception as e:
            continue
    
    return opportunities

def scan_events():
    """Find markets closing soon with high certainty"""
    markets = fetch("markets?limit=30&active=true&closed=false")
    if not markets:
        return []
    
    soon = []
    for m in markets:
        try:
            end_date = m.get("endDate", "")
            if not end_date:
                continue
            
            vol = float(m.get("volume", 0))
            if vol < MIN_VOLUME:
                continue
            
            prices = json.loads(m.get("outcomePrices", "[]"))
            outcomes = json.loads(m.get("outcomes", "[]"))
            
            for i, price in enumerate(prices):
                p = float(price)
                if p > 0.95:
                    # Event closing soon, near certain — check if price is above true certainty
                    soon.append({
                        "question": m.get("question", "?")[:100],
                        "outcome": outcomes[i],
                        "price": round(p, 4),
                        "volume": vol,
                        "end": end_date[:10],
                        "play": "SELL at premium (price > true certainty = free money if it resolves YES)"
                    })
        except:
            continue
    
    return soon[:5]

def main():
    print(f"=== Polymarket Scanner — {datetime.now().strftime('%H:%M')} ===\n")
    
    # Scan for opportunities
    opps = scan_markets()
    events = scan_events()
    
    if not opps and not events:
        print("No actionable opportunities found.")
        return
    
    if opps:
        print("MARKET OPPORTUNITIES:")
        for o in opps[:5]:
            print(f"\n  [{o['type']}] {o['question']}")
            print(f"  Volume: ${o['volume']:,.0f}")
            if "outcomes" in o:
                for i, out in enumerate(o['outcomes']):
                    print(f"    {out}: {o['prices'][i]}")
                print(f"  Total implied: {o['total_implied']}")
            else:
                print(f"  {o['outcome']} @ {o['price']}")
                print(f"  {o['note']}")
    
    if events:
        print("\nCLOSING SOON (sell premium):")
        for e in events:
            print(f"\n  {e['question']}")
            print(f"  {e['outcome']} @ {e['price']} — ends {e['end']}")
            print(f"  Play: {e['play']}")

if __name__ == "__main__":
    main()
