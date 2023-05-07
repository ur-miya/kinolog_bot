from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_app.states import GeneralStates
from . app import dp , bot
from . keyboards import inline_kb


@dp.callback_query_handler(lambda c: c.data in ['user'])
async def button_click_callback(callback_query:types.CallbackQuery, state:FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    await bot.send_message(callback_query.from_user.id, 'you are a user')

