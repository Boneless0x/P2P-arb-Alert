import requests
import os
import random

# === CONFIG ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Your exact niche
NICHE = "Crypto Discord Setup"

def generate_growth_pack():
    tweets = [
        "Just set up a Discord for a new memecoin that hit 1,800 members in 48 hours. The secret? 3 simple channels most projects miss. Thread 👇",
        "Crypto projects keep asking me: “Why is my Discord dead?” Here’s the #1 mistake I see in 90% of launch Discords →",
        "Free Crypto Discord Setup Checklist (2026 edition) – roles, bots, verification & growth hacks. DM me ‘CHECKLIST’ to get it.",
        "If your Discord still only has #general and #announcements, you’re losing members daily. Here’s the exact 9-channel structure I use for every project.",
        "Pro tip for crypto founders: Add a #p2p-trading or #alpha-calls channel on day 1. It turns lurkers into active members instantly.",
        "Thread: How to turn a dead Discord into a 5k+ engaged community before your token even launches (step-by-step)",
        "Poll: What’s the biggest Discord struggle for your crypto project right now? A) Dead chat B) No verification C) Bad bots D) Other",
        "Just helped a DeFi project go from 240 to 2,400 members in 3 weeks using only free tools. Want the exact blueprint? Reply ‘BLUEPRINT’",
        "Never pay for a Discord manager again. Here’s the exact role hierarchy + bot setup I use for every launchpad I work with.",
        "Quick win: Pin a ‘Welcome + Wallet Verification’ message with Collab.Land. I’ve seen this single change double daily active members."
    ]

    engagement = [
        "Reply to 5 tweets from crypto founders asking about Discord/community setup",
        "Quote-tweet any project announcing their token launch with a useful Discord tip",
        "Engage with the last 3 posts from @MEE6bot, @Collab_Land, @dyno",
        "Find accounts posting ‘need community manager’ or ‘Discord setup’ and offer value",
        "Post one value thread today and pin it to your profile"
    ]

    selected_tweets = random.sample(tweets, 5)

    message = f"""🚀 <b>YOUR DAILY X GROWTH PACK - CRYPTO DISCORD SETUP</b> 🚀

Niche: Crypto Projects’ Discord Setup

📝 5 Ready-to-Post Tweets/Threads:
"""
    for i, tweet in enumerate(selected_tweets, 1):
        message += f"\n{i}. {tweet}\n"

    message += f"\n\n🔥 Today’s Engagement Tasks (do at least 3):\n"
    for task in engagement:
        message += f"• {task}\n"

    message += "\n\nPost 3–5 times today + engage for 20–30 mins = fastest way to become the go-to Discord expert in crypto."

    return message

if __name__ == "__main__":
    print("🔄 Generating your Crypto Discord Setup Growth Pack...")
    pack = generate_growth_pack()
    
    tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": pack, "parse_mode": "HTML"}
    requests.post(tg_url, json=payload)
    print("✅ Growth Pack sent to your Telegram!")
