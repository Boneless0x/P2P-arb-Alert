import requests
import os

# === CONFIG ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
PROFIT_THRESHOLD = 0      # Lower to 3000 if you want more frequent alerts
TRADE_AMOUNT = 100

def get_p2p_offers(trade_type):
    url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    payload = {
        "asset": "USDT",
        "fiat": "NGN",
        "tradeType": trade_type,
        "page": 1,
        "rows": 20,
        "payTypes": [],
        "transAmount": "",
        "countries": [],
        "proMerchantAds": False,
        "shieldMerchantAds": False,
        "filterType": "all",
        "periods": [],
        "additionalKycVerifyFilter": 0,
        "publisherType": None,
        "merchantCheck": False,
        "classifies": ["mass", "profession", "fiat_trade"]
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://p2p.binance.com",
        "Referer": "https://p2p.binance.com/"
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        print(f"Status code for {trade_type}: {response.status_code}")
        print(f"Response preview: {response.text[:500]}...")  # shortened
        
        response.raise_for_status()
        data = response.json()
        
        offers = []
        for item in data.get("data", []):
            adv = item.get("adv", {})
            if not adv or float(adv.get("price", 0)) == 0:
                continue
            offers.append({
                "price": float(adv["price"]),
                "available": float(adv.get("surplusAmount", 0)),
                "min_trans": float(adv.get("minSingleTransAmount", 0)),
                "username": item.get("advertiser", {}).get("nickName", "Unknown"),
                "payments": [m.get("payMethodName", "") for m in item.get("payMethods", []) if m]
            })
        print(f"Found {len(offers)} offers for {trade_type}")
        return offers
    except Exception as e:
        print(f"ERROR fetching {trade_type}: {e}")
        if 'response' in locals():
            print(f"Raw response: {response.text[:600]}")
        return []

if __name__ == "__main__":
    print("🔄 Fetching live Binance P2P USDT/NGN rates...")

    sell_offers = get_p2p_offers("SELL")   # Buy cheap
    buy_offers  = get_p2p_offers("BUY")    # Sell expensive

    if not sell_offers or not buy_offers:
        print("Still no offers (rare).")
    else:
        valid_sell = [o for o in sell_offers if o["available"] > 50 and o["min_trans"] <= 200]
        min_buy_price = min((o["price"] for o in valid_sell), default=0)
        best_buy = min(valid_sell, key=lambda o: o["price"]) if valid_sell else None

        valid_buy = [o for o in buy_offers if o["available"] > 50 and o["min_trans"] <= 200]
        max_sell_price = max((o["price"] for o in valid_buy), default=0)
        best_sell = max(valid_buy, key=lambda o: o["price"]) if valid_buy else None

        spread = max_sell_price - min_buy_price
        profit = spread * TRADE_AMOUNT

        print(f"Buy at : {min_buy_price:.2f} NGN/USDT")
        print(f"Sell at: {max_sell_price:.2f} NGN/USDT")
        print(f"Profit on {TRADE_AMOUNT} USDT: ₦{profit:,.0f}")

        if profit > PROFIT_THRESHOLD and spread > 0 and best_buy and best_sell:
            message = f"""🚨 <b>P2P ARBITRAGE ALERT</b> 🚨

💰 Buy USDT at: <b>{min_buy_price:.2f}</b> NGN
👤 {best_buy['username']}

💰 Sell USDT at: <b>{max_sell_price:.2f}</b> NGN
👤 {best_sell['username']}

📈 Spread: {spread:.2f} NGN/USDT
💵 Profit on {TRADE_AMOUNT} USDT: <b>₦{profit:,.0f}</b>

🔗 Buy: https://p2p.binance.com/en/trade/sell/USDT?fiat=NGN
🔗 Sell: https://p2p.binance.com/en/trade/buy/USDT?fiat=NGN

Act fast!"""
            
            tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
            requests.post(tg_url, json=payload)
            print("✅ Alert sent to your Telegram!")
        else:
            print("No opportunity above ₦5,000 yet.")
