# ECG Telegram Bot

بوت تلغرام يستخدم الذكاء الاصطناعي للرد على أسئلة تخطيط القلب ECG.

## المتطلبات
- حساب OpenAI API Key
- حساب BotFather (Telegram bot token)

## طريقة التشغيل
1. ارفع المشروع إلى GitHub أو Railway.
2. في Variables بـ Railway:
   - `TELEGRAM_TOKEN` = ضع التوكن حق البوت.
   - `OPENAI_API_KEY` = ضع مفتاح OpenAI.
3. شغل المشروع.

## الأوامر
- `/start` للترحيب.
- أي رسالة نصية → يرد عليك باستخدام الذكاء الاصطناعي.
