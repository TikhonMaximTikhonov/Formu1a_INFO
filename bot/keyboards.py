from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def season_keyboard(season_list: list) -> InlineKeyboardMarkup:
    season_keyboard_list = []
    for season in season_list:
        season_keyboard_list.append([
            InlineKeyboardButton(text=str(season), callback_data=str(season))
        ])
    return InlineKeyboardMarkup(inline_keyboard=season_keyboard_list)


async def statistic_type_keyboard() -> InlineKeyboardMarkup:
    statistic_type_list = [
        [InlineKeyboardButton(text="Заезды", callback_data="races")],
        [
            InlineKeyboardButton(text="Команды", callback_data="teams"),
            InlineKeyboardButton(text="Пилоты", callback_data="drivers")
        ],
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=statistic_type_list)
