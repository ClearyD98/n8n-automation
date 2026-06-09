#!/usr/bin/env python3
"""Constant Polymarket scanner — finds edge, reports to Discord"""
import urllib.request, json, time, os, sys

def scan():
    try:
        req = urllib.request.Request(
            "https://gamma-api.polymarket.com/events?limit=20&order=volume&active=true&closed=false",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            events = json.loads(resp.read())
        
        signals = []
        for ev in events[:15]:
            volume = float(ev.get('volume', 0))
            if volume < 30000: continue
            title = ev.get('title', '?')
            for m in ev.get('markets', [])[:2]:
                q = m.get('question', '')
                try:
                    prices = json.loads(m.get('outcomePrices', '[]'))
                    if len(prices) >= 2:
                        yes = float(prices[0]); no = float(prices[1])
                        gap = abs(1.0 - (yes + no))
                        if gap >= 0.02:
                            direction = "BUY_NO" if (yes+no) > 1 else "BUY_YES"
                            signals.append(f"🎯 {gap*100:.1f}% | {direction} | {q[:80]} | Vol: ${volume:,.0f} | Yes:{yes*100:.1f}% No:{no*100:.1f}%")
                except: pass
        
        return signals
    except Exception as e:
        return [f"Scanner error: {e}"]

if __name__ == "__main__":
    print(f"Polymarket scanner started — {time.strftime('%H:%M:%S')}")
    signals = scan()
    if signals:
        for s in signals:
            print(s)
    else:
        print("No edge ≥2% on high-volume markets")
