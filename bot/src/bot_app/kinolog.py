from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_app.states import GeneralStates
from . app import dp , bot
from . keyboards import inline_kb, kb_kin_q, kb_kin_d
from . kinolog_form import k_form


@dp.callback_query_handler(lambda c: c.data in ['kinolog'])
async def registration_button_click(callback_query:types.CallbackQuery, state:FSMContext):
    await GeneralStates.kinolog.set()
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    await bot.send_message(callback_query.from_user.id, 'you are a kinolog\n Go to the /form')

@dp.message_handler(commands=['form'])
async def kinolog_form(message:types.Message):
    await message.answer('Question 1', reply_markup=kb_kin_q)

@dp.callback_query_handler(lambda c: c.data in ['ans1', 'ans2', 'ans3'])
async def button_click_callback(callback_query:types.CallbackQuery, state:FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    k_form.append(answer)
    await bot.send_message(callback_query.from_user.id, k_form)
    await bot.send_message(callback_query.from_user.id, 'Choose time', reply_markup=kb_kin_d)

@dp.callback_query_handler()
async def callback_choose_time(callback_query:types.CallbackQuery, state:FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    await bot.send_message(callback_query.from_user.id, f'The time {answer} was chosen successfully')
