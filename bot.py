from commands import bot
import os

if __name__ == "__main__":
    print("🤖 Text Analyzer Bot is starting...")
    try:
        bot_info = bot.get_me()
        print(f"✅ Bot is running! Username: @{bot_info.username}")
        print("✅ Waiting for messages...")
        bot.infinity_polling()
    except Exception as e:
        print(f"❌ Error: {e}")
