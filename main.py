from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='1522832988:AAEqflIFIPDPiim_JCNyjQK5B0FcjoSnvxg')
dp = Dispatcher(bot)


@dp.message_handler()
async def get_massage(message: types.Message):
    chat_id = message.chat.id
    # text = 'hello'
    # await bot.send_message(chat_id=chat_id, text=text)
    link = await bot.get_me()
    print(link.username)


executor.start_polling(dp)
