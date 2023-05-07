from aiogram.dispatcher.filters.state import State, StatesGroup

class GeneralStates(StatesGroup):
    start = State()
    kinolog = State()
    user = State()