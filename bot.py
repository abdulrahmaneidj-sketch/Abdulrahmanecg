import os
import telebot
from openai import OpenAI

# ضع التوكنات حقتك هنا
TELEGRAM_TOKEN = "ضع_توكن_بوت_التلقرام"
OPENAI_API_KEY = "ضع_مفتاح_OpenAI"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # استدعاء موديل OpenAI الجديد
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # تقدر تبدلها بـ gpt-4o لو تبي أقوى
            messages=[
                {"role": "system", "content": "انت بوت مختص بشرح تخطيط القلب (ECG). تجاوب بالعربية أو الإنجليزية باختصار ودقة."},
                {"role": "user", "content": message.text}
            ]
        )

        reply = response.choices[0].message.content
        bot.reply_to(message, reply)

    except Exception as e:
        bot.reply_to(message, f"صار خطأ: {str(e)}")

print("✅ البوت شغّال ...")
bot.polling()
