from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я ваш Telegram бот. Введите /roulette, чтобы испытать удачу!")

# Обработчик команды /roulette
async def roulette(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Список возможных результатов (можно добавить ссылки на изображения или текстовые сообщения)
    outcomes = [
        "Поздравляю! Вы выиграли приз!",
        "Упс, ничего не выпало. Попробуйте еще раз!",
        "Удача на вашей стороне! Вы получаете бонус!",
        "Вы выиграли скидку!",
        "К сожалению, вы проиграли.",
        "Сегодня ваш день! Получите специальный подарок!"
    ]
    
    # Выбираем случайный результат
    result = random.choice(outcomes)
    
    # Отправляем результат пользователю
    await update.message.reply_text(result)

# Основной код для запуска бота
if __name__ == "__main__":
    # Вставьте ваш токен вместо "YOUR_TOKEN_HERE"
    app = ApplicationBuilder().token("7875175438:AAFGr4ho2Ey9cgx-ypiP-dIQ4AnWKQQZXvE").build()

    # Добавляем обработчики команд /start и /roulette
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("roulette", roulette))

    # Запускаем бота
    print("Бот запущен!")
    app.run_polling()
