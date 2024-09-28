from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def season_keyboard(season_list: list) -> InlineKeyboardMarkup:
    season_keyboard_list = []
    for season in season_list:
        season_keyboard_list.append([
            InlineKeyboardButton(text=str(season), callback_data=str(season))
        ])
    return InlineKeyboardMarkup(inline_keyboard=season_keyboard_list)
