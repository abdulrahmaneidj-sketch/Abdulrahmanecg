import os
import telebot
import openai

# جلب التوكن من المتغيرات البيئية
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "مرحباً 👋 أنا بوت ECG مع أبو عيد. اسألني أي شيء يخص تخطيط القلب!")

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        user_message = message.text

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "انت مساعد مختص في ECG. اجعل إجاباتك دقيقة ومباشرة."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=300,
            temperature=0.7
        )

        reply = response["choices"][0]["message"]["content"]
        bot.reply_to(message, reply)

    except Exception as e:
        bot.reply_to(message, f"حدث خطأ: {str(e)}")

# تشغيل البوت
bot.polling()
