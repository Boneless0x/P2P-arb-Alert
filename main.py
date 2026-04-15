import requests
import os
import random

# === CONFIG ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def generate_growth_pack():
    tweets = [
        "Crypto founders: your Discord is probably killing your project and you don’t even know it. The #1 mistake I fix in every setup →",
        "Just built a Discord that went from 0 to 2,800 members in 18 days for a new launchpad. Here’s the exact channel structure I used.",
        "Free 2026 Crypto Discord Setup Checklist – roles, bots, verification & growth system. DM me ‘CHECKLIST’",
        "If your Discord only has #general and #announcements, you’re losing 70% of potential members. Here’s what actually works.",
        "Pro move: Add a #p2p-trading or #alpha-calls channel on day 1. Turns lurkers into daily active users instantly."
    ]

    threads = [
        """Thread: How to Build a Crypto Discord That Actually Grows (2026 Edition)

1/ Most projects launch with 5 channels and wonder why it’s dead.
2/ Here’s the exact 11-channel structure I use for every paid setup.
3/ #welcome + auto verification with Collab.Land
4/ #announcements (admins only)
5/ #general-chat + #memes
6/ #alpha-calls + #p2p-trading (huge for engagement)
7/ #support-tickets + #verify
8/ Voice: Lounge + AMA Stage
9/ The secret? Role hierarchy + daily content calendar.
10/ Want me to set yours up? DM ‘SETUP’""",

        """Thread: The Discord Mistake Killing 90% of Crypto Projects

1/ They copy big servers and add 20 channels on day 1.
2/ New members get overwhelmed and leave.
3/ My rule: Start with ONLY 7 channels max.
4/ Focus on verification + one high-engagement channel first.
5/ I’ve seen this single change 3x daily active members.
6/ Want the full blueprint + bot list? Reply ‘BLUEPRINT’"""
    ]

    image_ideas = [
        "Clean screenshot of a professional Discord server dashboard showing verified roles, welcome channel, and announcement pinned (green + purple color scheme)",
        "Before vs After Discord server comparison - left side messy with 20 channels, right side clean 9-channel setup",
        "Infographic: Crypto Discord Growth Funnel - from visitor to verified member to active trader",
        "Minimalist graphic with text 'Crypto Discord Setup Checklist 2026' on dark background with neon accents"
    ]

    engagement = [
        "Reply to 5 tweets from crypto founders saying 'launching soon' or 'need community help'",
        "Quote-tweet any project announcing their token with a useful Discord tip",
        "Engage with recent posts from @MEE6bot, @Collab_Land, @TicketTool",
        "Find accounts posting 'Discord setup' or 'community manager needed' and offer value",
        "Post one thread today and pin it to your profile"
    ]

    selected_tweets = random.sample(tweets, 5)
    selected_threads = random.sample(threads, 2)
    selected_images = random.sample(image_ideas, 3)

    message = f"""🚀 <b>YOUR DAILY X GROWTH PACK - CRYPTO DISCORD SETUP</b> 🚀

📝 5 Ready-to-Post Tweets:
"""
    for i, tweet in enumerate(selected_tweets, 1):
        message += f"\n{i}. {tweet}\n"

    message += f"\n\n🧵 2 Full Thread Templates (copy-paste ready):\n"
    for i, thread in enumerate(selected_threads, 1):
        message += f"\nThread {i}:\n{thread}\n"

    message += f"\n\n🖼️ Image Ideas (copy-paste into Grok Imagine):\n"
    for i, idea in enumerate(selected_images, 1):
        message += f"\n{i}. {idea}\n"

    message += f"\n\n🔥 Today’s Engagement Tasks (do at least 3):\n"
    for task in engagement:
        message += f"• {task}\n"

    message += "\n\nPost 3–5 tweets + 1 thread today. Use the image ideas for higher reach. This is how you become the go-to Crypto Discord expert."

    return message

if __name__ == "__main__":
    print("🔄 Generating your Crypto Discord Setup Growth Pack...")
    pack = generate_growth_pack()
    
    tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": pack, "parse_mode": "HTML"}
    requests.post(tg_url, json=payload)
    print("✅ Growth Pack sent to your Telegram!")
