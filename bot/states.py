from aiogram.fsm.state import State, StatesGroup


class User(StatesGroup):
    season = State()
    statistic_type = State()

