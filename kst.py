from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.webhook_info import WebhookInfo

bot = Bot('7462129540:AAE4Iuxls36pty-q09Z6IirNQ8Q1P-LjsOA')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('запуск', web_app=WebhookInfo(url='https://google.com')))
    await message.answer('Hi',reply_markup=markup)

executor.start_polling(dp)
