# импорты ########################################################################################
import asyncio                                                                                  ##
from aiogram import Bot, Dispatcher, types, Router                                              ##
from aiogram.types import Message                                                               ##
from aiogram.filters import Command, CommandStart                                               ##
from random import choice                                                                       ##
import time                                                                                     ##
import sqlite3 as sq                                                                            ##
from sqlalchemy.orm import DeclarativeBase, Mapped                                              ##
from sqlalchemy.orm import mapped_column                                                        ##
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine          ##
from belka.dbmain import async_main#*, sync_user                                                  ##
##################################################################################################


saytxt = ['Мяу', 'Мур', 'Мр-р', 'Мя-а-а', 'Мяф', 'Ме', 'Иди на GreenLightStudio']

bot = Bot(token='token')
dp = Dispatcher()
router = Router()


async def main():
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)



@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Aiogram ✅    Script ✅   DB ✅')
#*    await sync_user(message.from_user.id) 



@dp.message(Command('pet'))
async def pet(message: Message):
    await message.answer('Мурчит')
    await message.answer('Вы погладили Белочку')

@dp.message(Command('feed'))
async def feed(message: Message):
    await message.answer('Кушает')
    time.sleep(3)
    await message.answer('Вы покормили Белочку')

@dp.message(Command('say'))
async def say(message: Message):
    await message.answer(choice(saytxt))

@dp.message(Command('clog'))
async def clog(message: Message):
    await message.answer('0.2: добавлены команды /ver, /clog, /hit (/kick), /redeem')
    await message.answer('0.2.1: Белка полностью перенесена на библиотеку AioGram (раньше была pyTelegramBotApi)')

@dp.message(Command('rep'))
async def rep(message: Message):
    await message.answer('WIP')

@dp.message(Command('ударить', 'пнуть', 'hit', 'kick'))
async def hit(message: Message):
    await message.answer('МЯФК')
    await message.answer('Шипит')
    await message.answer('Вы ударили Белочку')
    await message.answer('(Как вы могли)')

@dp.message(Command('ver'))
async def ver(message: Message):
    await message.answer('current version is 0.2.1')
    await message.answer('type /clog to see changelog')

@dp.message(Command('play'))
async def a(message: Message):
    await message.answer('Тыгдык-тыгдык')
    await message.answer('Прыг')
    await message.answer('Тыгдык-тыгдык')
    await message.answer('Кусь')
    await message.answer('Вы поиграли с Белочкой')




if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Script stopped')
