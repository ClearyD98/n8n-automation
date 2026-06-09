#!/usr/bin/env python3
"""Autoprod Gambler - Scan Polymarket for edges and report"""
import urllib.request, urllib.error, json, time, os, sys

GAMMA_URL = "https://gamma-api.polymarket.com"
CLOB_URL = "https://clob.polymarket.com"

MIN_VOLUME = 50000
MIN_EDGE = 0.03
MAX_BET = 5.00
BANKROLL = 14.00

API_KEY = os.environ.get("POLYMARKET_API_KEY", "")
API_SECRET = os.environ.get("POLYMARKET_SECRET", "")
API_PASSPHRASE = os.environ.get("POLYMARKET_PASSPHRASE", "")

def gamma_request(path):
    req = urllib.request.Request(f"{GAMMA_URL}{path}", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

def clob_book(token_id):
    req = urllib.request.Request(
        f"{CLOB_URL}/book?token_id={token_id}",
        headers={
            "User-Agent": "Mozilla/5.0",
            "POLY_API_KEY": API_KEY,
            "POLY_SECRET": API_SECRET,
            "POLY_PASSPHRASE": API_PASSPHRASE,
        }
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

def scan():
    report = []
    now = time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())
    report.append("GAMBLER REPORT - " + now)
    report.append("Bankroll: 14.00")
    report.append("")

    try:
        events = gamma_request("/events?limit=50&closed=false&active=true&order=volume")
    except Exception as e:
        report.append("Scan failed: " + str(e))
        return "\n".join(report)

    real_events = [e for e in events if float(e.get('volume', 0)) > MIN_VOLUME]
    real_events.sort(key=lambda e: float(e.get('volume', 0)), reverse=True)

    report.append("Scanned " + str(len(real_events)) + " events with >$50k volume")
    report.append("")

    opportunities = []

    for ev in real_events:
        volume = float(ev.get('volume', 0))
        title = ev.get('title', '?')[:60]

        for m in ev.get('markets', []):
            try:
                prices = json.loads(m.get('outcomePrices', '[]'))
                token_ids = json.loads(m.get('clobTokenIds', '[]'))

                if len(prices) < 2 or len(token_ids) < 2:
                    continue

                yes, no = float(prices[0]), float(prices[1])
                total = yes + no
                gap = abs(1.0 - total)

                if gap >= MIN_EDGE:
                    direction = "NO" if total > 1 else "YES"
                    idx = 1 if direction == "NO" else 0
                    opp = {
                        "question": m.get('question', '?'),
                        "direction": direction,
                        "price": float(prices[idx]),
                        "token_id": token_ids[idx],
                        "gap": gap,
                        "volume": volume,
                        "title": title,
                    }
                    opportunities.append(opp)
                    continue

                if token_ids[0]:
                    try:
                        book_yes = clob_book(token_ids[0])
                        book_no = clob_book(token_ids[1])

                        bids_yes = book_yes.get('bids', [])
                        asks_yes = book_yes.get('asks', [])
                        bids_no = book_no.get('bids', [])
                        asks_no = book_no.get('asks', [])

                        if bids_yes and asks_yes and bids_no and asks_no:
                            yes_bid = float(bids_yes[0]['price'])
                            yes_ask = float(asks_yes[0]['price'])
                            no_bid = float(bids_no[0]['price'])
                            no_ask = float(asks_no[0]['price'])

                            buy_cost = yes_ask + no_ask
                            sell_value = yes_bid + no_bid
                            buy_arb = 1.0 - buy_cost
                            sell_arb = sell_value - 1.0

                            if buy_arb >= MIN_EDGE:
                                opportunities.append({
                                    "question": m.get('question', '?'),
                                    "direction": "BUY_BOTH",
                                    "price": buy_cost,
                                    "gap": buy_arb,
                                    "volume": volume,
                                    "title": title,
                                    "detail": "Buy YES@" + str(yes_ask) + " + NO@" + str(no_ask) + " = " + str(round(buy_cost, 4)),
                                })
                            if sell_arb >= MIN_EDGE:
                                opportunities.append({
                                    "question": m.get('question', '?'),
                                    "direction": "SELL_BOTH",
                                    "price": sell_value,
                                    "gap": sell_arb,
                                    "volume": volume,
                                    "title": title,
                                    "detail": "Sell YES@" + str(yes_bid) + " + NO@" + str(no_bid) + " = " + str(round(sell_value, 4)),
                                })
                    except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError):
                        pass
            except:
                pass

    try:
        events2 = gamma_request("/events?limit=100&closed=false&active=true&tag=sports")
        for ev in events2:
            title = ev.get('title', '')
            if 'World Cup Winner' in title:
                markets = ev.get('markets', [])
                prices_list = []
                for m in markets:
                    try:
                        p = json.loads(m.get('outcomePrices', '[]'))
                        if len(p) >= 2:
                            prices_list.append(float(p[0]))
                    except:
                        pass
                if prices_list:
                    total_prob = sum(prices_list)
                    if abs(total_prob - 1.0) >= 0.02:
                        opportunities.append({
                            "question": "Multi-market: " + title,
                            "direction": "ARB",
                            "price": total_prob,
                            "gap": abs(total_prob - 1.0),
                            "volume": float(ev.get('volume', 0)),
                            "detail": "Sum of all Yes prices = " + str(round(total_prob*100, 1)) + "% (should be ~100%)",
                        })
    except:
        pass

    opportunities.sort(key=lambda x: x['gap'], reverse=True)

    if opportunities:
        report.append("OPPORTUNITIES FOUND")
        report.append("")
        for opp in opportunities:
            q = opp.get('question', '?')[:70]
            gap_pct = round(opp['gap'] * 100, 1)
            vol = opp.get('volume', 0)
            detail = opp.get('detail', '')
            report.append("* " + q)
            if detail:
                report.append("  " + detail + " | Edge: " + str(gap_pct) + "% | Vol: $" + "{:,.0f}".format(vol))
            else:
                report.append("  Buy " + opp['direction'] + " @ " + str(round(float(opp['price'])*100, 1)) + "c | Edge: " + str(gap_pct) + "% | Vol: $" + "{:,.0f}".format(vol))
            report.append("")

        best = opportunities[0]
        if best['gap'] >= MIN_EDGE and best.get('token_id'):
            bet = min(MAX_BET, BANKROLL * 0.33)
            report.append("ATTEMPTING TRADE...")
            report.append("  Market: " + best['question'][:60])
            report.append("  Side: " + best['direction'])
            report.append("  Amount: " + str(round(bet, 2)))
            report.append("  Edge: " + str(round(best['gap']*100, 1)) + "%")

            try:
                order = {
                    "token_id": best['token_id'],
                    "price": str(best['price']),
                    "side": "BUY",
                    "size": str(bet),
                }
                req = urllib.request.Request(
                    CLOB_URL + "/order",
                    data=json.dumps(order).encode(),
                    headers={
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0",
                        "POLY_API_KEY": API_KEY,
                        "POLY_SECRET": API_SECRET,
                        "POLY_PASSPHRASE": API_PASSPHRASE,
                    },
                    method="POST"
                )
                with urllib.request.urlopen(req, timeout=15) as resp:
                    result = json.loads(resp.read())
                    report.append("  TRADE EXECUTED: " + result.get('status', 'filled'))
            except urllib.error.HTTPError as e:
                err = e.read().decode()[:200]
                report.append("  Trade FAILED: HTTP " + str(e.code) + " - " + err)
            except Exception as e:
                report.append("  Trade FAILED: " + str(e))
        elif best['gap'] >= MIN_EDGE:
            report.append("Best opportunity requires multi-leg arb (not executable)")
        else:
            report.append("No tradable edge meeting criteria")
    else:
        report.append("No edge today. All markets efficiently priced.")

    report.append("")
    report.append("---")
    report.append("WINNERS THIS SESSION: none")
    report.append("LIFETIME P&L: 0.00")
    report.append("Bankroll: 14.00")

    return "\n".join(report)

if __name__ == "__main__":
    print(scan())
