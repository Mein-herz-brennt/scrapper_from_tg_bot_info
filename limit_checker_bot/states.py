from aiogram.dispatcher.filters.state import StatesGroup, State


class CardLimitChecker(StatesGroup):
    file_with_cards = State()