import requests
from bs4 import BeautifulSoup
import os
import re

# === CONFIG ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
PROFIT_THRESHOLD = 5000
TRADE_AMOUNT = 100

def get_remitano_prices():
    url = "https://remitano.net/ng/p2p/usdt"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        # Improved regex that catches prices after ###### and normal decimal prices
        price_pattern = r'(?:######\s*)?(\d{1,3}(?:,\d{3})*\.\d{2})'
        prices = [float(x.replace(',', '')) for x in re.findall(price_pattern, text) if 1000 < float(x.replace(',', '')) < 2000]

        if not prices:
            print("No prices found on page")
            print("Page preview (first 300 chars):", text[:300])
            return None, None

        min_buy = min(prices)   # Cheapest to BUY USDT
        max_sell = max(prices)  # Most expensive to SELL USDT

        print(f"Found {len(prices)} prices on page")
        print(f"Lowest buy price : {min_buy:.2f} NGN/USDT")
        print(f"Highest sell price: {max_sell:.2f} NGN/USDT")
        return min_buy, max_sell

    except Exception as e:
        print(f"Error fetching Remitano: {e}")
        return None, None

if __name__ == "__main__":
    print("🔄 Fetching live Remitano P2P USDT/NGN rates...")

    min_buy, max_sell = get_remitano_prices()

    if min_buy is None or max_sell is None:
        print("No offers right now.")
    else:
        spread = max_sell - min_buy
        profit = spread * TRADE_AMOUNT

        print(f"Buy at : {min_buy:.2f} NGN/USDT")
        print(f"Sell at: {max_sell:.2f} NGN/USDT")
        print(f"Profit on {TRADE_AMOUNT} USDT: ₦{profit:,.0f}")

        if profit > PROFIT_THRESHOLD and spread > 0:
            message = f"""🚨 <b>REMITANO P2P ARBITRAGE ALERT</b> 🚨

💰 Buy USDT at: <b>{min_buy:.2f}</b> NGN
💰 Sell USDT at: <b>{max_sell:.2f}</b> NGN

📈 Spread: {spread:.2f} NGN/USDT
💵 Profit on {TRADE_AMOUNT} USDT: <b>₦{profit:,.0f}</b>

🔗 Open Remitano P2P: https://remitano.net/ng/p2p/usdt

Act fast!"""

            tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
            requests.post(tg_url, json=payload)
            print("✅ Alert sent to your Telegram!")
        else:
            print("No opportunity above ₦5,000 yet.")
