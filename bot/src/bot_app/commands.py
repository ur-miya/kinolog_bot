from aiogram import types
from .app import dp
from . import messages
from . keyboards import inline_kb



@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    await message.answer(messages.WELCOME_MESSAGE)

@dp.message_handler(commands=['help'])
async def send_help(message:types.Message):
    await message.answer(messages.HELP_MESSAGE)

@dp.message_handler(commands=['registraition'])
async def send_registration(message:types.Message):
    await message.answer(messages.REGISTRATION_MESSAGE, reply_markup=inline_kb)