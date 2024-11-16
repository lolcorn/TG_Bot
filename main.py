
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7510254418:AAEWQEdXNFQvmBEtAq4bRVRBV0__gFzXpGk"
bot = Bot (token = api)
Dispatcher (bot, storage= MemoryStorage())
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью')

@dp.message_handler()
async def all_massage(message):
    print('Введите команду /start, чтобы начать общение')



if __name__ == "__main__":
    executor.start_polling (dp, skip_updates=True)