import requests
import os
import random

# === CONFIG ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Your niche – change this line to whatever you want
NICHE = "crypto P2P arbitrage Nigeria"   # ←←← CHANGE THIS TO YOUR NICHE

def generate_growth_pack():
    # This is where the magic happens – tailored content ideas
    packs = {
        "crypto P2P arbitrage Nigeria": [
            "Just caught a ₦8,200 spread on Bybit vs Remitano in 11 minutes 👀 Who else is flipping USDT today? Drop your best platform below.",
            "Thread: How I turned ₦150k into ₦380k in one week with P2P (no gambling, no signals). Step 1–5 inside 👇",
            "Pro tip for Nigeria: The biggest P2P spreads happen between 6–9 AM and 8–11 PM. Set your alerts accordingly.",
            "If you’re still manually checking rates every hour, you’re leaving money on the table. Here’s the 15-minute scanner I use →",
            "Quick poll: What’s your main payment method for P2P right now? Opay / PalmPay / Bank transfer / Other"
        ]
        # Add more niches later if you want
    }
    
    tweets = packs.get(NICHE.lower(), packs["crypto P2P arbitrage Nigeria"])
    selected_tweets = random.sample(tweets, 5)
    
    # Engagement tasks (ethical)
    engagement = [
        "Like + reply to the last 3 posts from @binance, @Bybit_Official, @remitano",
        "Quote-tweet any P2P success story you see with your own tip",
        "Reply to 5 people asking about USDT rates today",
        "Find 3 new Nigerian crypto accounts posting today and engage genuinely",
        "Post one value thread and pin it"
    ]
    
    message = f"""🚀 <b>YOUR DAILY X GROWTH PACK</b> 🚀

Niche: {NICHE}

📝 5 Ready-to-Post Tweets:
"""
    for i, tweet in enumerate(selected_tweets, 1):
        message += f"\n{i}. {tweet}\n"
    
    message += f"\n\n🔥 Engagement Tasks (do 3–5 of these):\n"
    for task in engagement:
        message += f"• {task}\n"
    
    message += "\n\nPost 3–5 times today + engage for 20–30 mins = fastest organic growth with zero risk."
    
    return message

if __name__ == "__main__":
    print("🔄 Generating your X Growth Pack...")
    pack = generate_growth_pack()
    
    tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": pack, "parse_mode": "HTML"}
    requests.post(tg_url, json=payload)
    print("✅ Growth Pack sent to your Telegram!")
