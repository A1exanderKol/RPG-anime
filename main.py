import logging
from aiogram import Bot, Dispatcher, types, executor
import config
import keyboard
import dbwork
import levels
import traceback

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(messege: types.Message):
    await messege.answer('Добро пожаловать в рпг-анимешника!'
                         '\nЕсли здесь новенький и не знаешь, что делать, нажми => /help', reply_markup = keyboard.kb)
    await messege.answer('Welcome to the rpg-animeshnik!'
                        '\n If you are new here and do not know what to do, click => /help')
    id = messege.from_user.id
    dbwork.strt(id)



@dp.message_handler(commands=['help'])
async def start(messege: types.Message):
    await messege.answer('Напиши название аниме боту и количество серий через - (пример: название-кол.эпизод)'
                         '\nПосмотреть профиль: /PROFILE'
                         '\nПросмотренные аниме: /SHOW')
    await messege.answer('Write the name of the anime bot and the number of episodes via - (example: title-count episode)'
                        '\nView profile: /PROFILE'
                        '\nView anime: /SHOW')


@dp.message_handler(commands=['PROFILE'])
async def pr(messege: types.Message):
    id = messege.from_user.id
    e, l = dbwork.prf(id)
    await messege.answer(f'level: {l}'
                        f'\n exp: {e}')



@dp.message_handler(commands=['SHOW'])
async def sh(messege: types.Message):
    id = messege.from_user.id
    await messege.answer(dbwork.shw(id))



@dp.message_handler()
async def watch (messege: types.Message):
    id = messege.from_user.id
    s= messege.text.split('-')
    name = s[0]
    epesods=int(s[1])
    exp = levels.opt_epe(epesods)
    dbwork.l_e_v(id,exp)
    return dbwork.wtch(id, name, epesods, exp)

while True:
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception:
        print(traceback.format_exc())
        continue

