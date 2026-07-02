import os

# Get bot token from environment variable (Railway)
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Check if token exists
if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN environment variable not set!")
    print("Please set BOT_TOKEN in Railway variables")
    exit(1)

print("✅ BOT_TOKEN loaded successfully!")
