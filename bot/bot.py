from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import asyncio
from json import loads

from states import User
from keyboards import *
from database.database import DataBase



bot = Bot(token=TOKEN)
dp = Dispatcher()

with open("texts.json", "r", encoding="utf8") as file:
    texts = loads(file.read())


@dp.message(F.text.contains("/start"))
async def season_choice(message: Message, state: FSMContext):
    await state.set_state(User.season)

    await message.answer(
        texts["start"],
        reply_markup=await season_keyboard()
    )


@dp.message(User.season)
async def statistic_type_choice(message: Message, state: FSMContext):
    await state.update_data(season=message.text)
    await state.set_state(User.statistic_type)

    data = await state.get_data()
    await message.answer(
        data.get("season")
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    data_base = DataBase("../database/database.db")
    print("Bot start!")
    asyncio.run(main())
