import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from json import loads

from states import User
from keyboards import *
from database.database import DataBase
from parser.parser import *

TOKEN = "7992264590:AAFcgIUuG-GWUhsKJGGk6ZDkBvVmyEbcgec"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text.contains("/start"))
async def season_choice(message: Message, state: FSMContext):
    await state.set_state(User.season)

    await message.answer(
        texts["season"],
        reply_markup=await season_keyboard(data_base.get_seasons())
    )


@dp.callback_query(F.data.startswith('20') and F.data.len() == 4, User.season)
async def statistic_type_choice(callback: CallbackQuery, state: FSMContext):
    await state.update_data(season=callback.data)
    await state.set_state(User.statistic_type)

    await callback.message.edit_text(
        texts["statistic_type"].filter(data_base.get_season_statistic()),
        reply_markup=await statistic_type_keyboard()
    )


@dp.message(F.text.contains("/update"))
async def update_info(message: Message):
    await message.answer(
        parse_season(message.text.split()[1])
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    with open("texts.json", "r", encoding="utf8") as file:
        texts = loads(file.read())

    data_base = DataBase("../database/database.db")
    print("Bot start!")
    # data_base.get_season_statistic(2024)
    asyncio.run(main())
