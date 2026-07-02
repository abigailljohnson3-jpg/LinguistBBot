from commands import bot
import os

if __name__ == "__main__":
    print("🤖 Text Analyzer Bot is starting...")
    print("✅ Bot is running! Waiting for messages...")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"❌ Error: {e}")
