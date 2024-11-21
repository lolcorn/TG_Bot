from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = "7510254418:AAEWQEdXNFQvmBEtAq4bRVRBV0__gFzXpGk"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button_2 = KeyboardButton(text="Информация")
kb.row(button, button_2)


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст')
    await UserStates.age.set()

@dp.message_handler(state=UserStates.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserStates.growth.set()

@dp.message_handler(state=UserStates.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserStates.weight.set()


@dp.message_handler(state=UserStates.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    Calories_man = int(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    Calories_wom = int(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161)
    await message.answer(f'Кол-во калорий для М: {Calories_man}')
    await message.answer(f'Кол-во калорий для Ж: {Calories_wom}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью'
                         'Для старта нажмите на кнопку: Рассчитать', reply_markup= kb)

@dp.message_handler(text="Информация")
async def set_gender(message):
    await message.answer(f"Бот, который помогает пользователю рассчитывать норму калорий "
                         f"в зависимости от его пола, возраста, роста и веса")




@dp.message_handler()
async def all_massage(message):
    await message.answer('Введите команду /start, чтобы начать общение')



if __name__ == "__main__":
    executor.start_polling (dp, skip_updates=True)