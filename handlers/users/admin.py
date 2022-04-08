import asyncio
import os
import random
from random import randint
from telethon import TelegramClient, Button, events 
from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from telethon.tl.functions.messages import ImportChatInviteRequest
from aiogram.utils.exceptions import Unauthorized
from telethon.tl.functions.channels import JoinChannelRequest
import json
from typing import Any, NoReturn
from telethon import TelegramClient, Button, events 
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os, time
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.users import GetUsersRequest
from telethon.tl.types import ChannelParticipantsSearch
import asyncio
import datetime, sys
from datetime import datetime, date, time
from telethon import utils
from telethon.tl.types import InputPeerUser
import os
from loguru import logger
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from convert_tdata import convert_tdata
import time
from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from telethon.errors.rpcerrorlist import FloodWaitError
from keyboards.inline.menu import back_admin, admin_menu, choose_menu
from loader import dp, bot
from states.states import BroadcastState, GiveTime, TakeTime
from keyboards.inline.menu import back_to_main_menu,  api_hash, api_id, code_menu, \
    main_menu, proxy_menu, start_spam_menu, accept_spam_menu, ssttop
from utils.db_api.db_commands import select_all_users, del_user, update_date
from calendar import c
from email import message
import random
from telethon.sessions import StringSession
from telethon.tl.custom import Button
from datetime import datetime
from telethon.tl.functions.channels import InviteToChannelRequest
import asyncio
from keyboards.inline.menu import back_to_main_menu,  api_hash, api_id, code_menu, \
    main_menu, proxy_menu, start_spam_menu, accept_spam_menu, inv
import socks
from utils.db_api.db_commands import select_all_users, del_user, update_date
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputChannel
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from aiogram.dispatcher import FSMContext
from telethon.tl.functions.messages import AddChatUserRequest
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import os, sys
import configparser
import csv
import time
import random

from lib2to3.pgen2 import token
import rarfile
import shutil
import re
import requests
from datetime import datetime
import time
from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import Bot, types, executor
from aiogram.utils.markdown import hbold, hlink
import time
from threading import Timer
import os
from telethon.sync import TelegramClient
from telethon import functions, types
from datetime import datetime, timedelta


class akasil(StatesGroup):
    sms_text = State()

class sms5(StatesGroup):
    sms_text = State()

class sms4(StatesGroup):
    sms_text = State()

class sms3(StatesGroup):
    sms_text = State()

class sms2(StatesGroup):
    sms_text = State()

class post(StatesGroup):
    text = State()

class tima(StatesGroup):
    timeout = State()
@dp.callback_query_handler(text="paussa")
async def paus(call: CallbackQuery):
    await call.message.answer("⏱    <b>Введи значение для паузы между отправкой смс 'меньше 30 сек не рекоминдую спам'</b>", reply_markup=back_to_main_menu)
    @dp.message_handler(content_types=['text'])
    async def paus(message: Message):
        pausse = message.text
        with open('time.txt', 'w') as f:
            f.write(pausse)
        await message.answer(f"⏱    <b>Тайминг Изменен на {pausse}</b>", reply_markup=back_to_main_menu)





@dp.callback_query_handler(text="rep")
async def rep(call: CallbackQuery):
    msms = await call.message.answer("<b>Запуск Reporter</b>")
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    tt = open('time.txt', 'r')
    ti = int(tt.read())
    tt.close()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    count = int(z)
    i = 1
    s = 0
    c = 0
    o = 0
    msm = 0
    a = 5
    while i <= xx:
        try:
            sto = open('stop.txt', 'r').read()
            if sto == 'stop':
                with open('stop.txt', 'w') as f:
                    f.write("start")
                await call.message.answer("Рассылка остановлена", reply_markup=back_to_main_menu)
                break
            if a == count:
                await client.disconnect()
                i = i + 1
                a = 0
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            cli = open(f"sessions/{acaunt}").read()
            aka = acaunt.split(".")[0]
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            ss = open('ussers.txt', 'r').readlines()
            username = ss[a][:-1]
            message_id = "8" 
            rsn = types.InputReportReasonPornography()
            msg = "some messages"
            async def rep(username, message_id, rsn, msg):
                print("y") 
                a = await client(functions.messages.ReportRequest(
                    peer='@'+username,
                    id=[int(message_id)],
                    reason=rsn,
                    message = msg
                ))
                print(a)

            msm = msm + 1
            await msms.edit_text(
                f"<b>   Всего отправленно жалоб {msm}</b>\n\n"
                f"💬    <b>Жалоба С Акаунта: \n<code>{aka}</code> \nна</b> <code>{username}</code> Отправленна! +1 \n\n", reply_markup=ssttop)
            o = o + 1
            
            mm = mm + 1
            time.sleep(ti)
            a = a + 1
            await client.disconnect()
        except:
            i = i + 1
    await call.message.answer("<b>Report Завершил работу над списком !</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="add_silka", state="*")
async def add_silka(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(
        f"<b>Для загрузки акаунтов по ссылке</b>\n"
        f"<b>Нужны акаунты только с этого ресурса:</b>\n"
        f"<b>https://ydeda.pro/</b>")
    await akasil.sms_text.set()




@dp.message_handler(state=akasil.sms_text)
async def receive_com(message: Message, state: 
    ww = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"
    API_ID = 17463049
    sessions = []
    await message.answer("<b>Идет Обработка и подвязка акаунтов ожидайте...</b>")
    baza = []
    print("".join(map(str, ww)))
    url_pattern = r'https://[\S]+'
    u = re.findall(url_pattern, ww)
    s = len(u)
    
    await message.answer(f"<b>Подготавливаю {s} Акаунтов</b>")
    for x in u:
        
        os.system(f"curl -k -L --output temp_aka/telega.rar  {x}")
        time.sleep(4)
        rar_file = "temp_aka/telega.rar"
        dir_name = "tdatas"
        rarobj = rarfile.RarFile(rar_file)
        rarobj.extractall(dir_name)
        xx = os.listdir(dir_name)
#        
#
        os.system(f"rm -r data\{xx[0]}")

        for tdata in os.listdir("tdatas"):
#            
            try:
                auth_key = convert_tdata(f"tdatas/{tdata}/tdata")[0]
            except Exception as err:
                logger.error(err)
            else:
                logger.success(f"{tdata} успешно конвертировано")

            sessions.append(StringSession(auth_key))

            logger.info("Проверка аккаунтов")
            j = 0
            for session in sessions:
                await message.edit_text(f"<b>Подключаю Акаунт № {xx[j]}</b>")
                j = j + 1
                client = TelegramClient(
                    session,
                    api_hash=API_HASH,
                    api_id=API_ID
                )

                

                await client.connect()
                auth_key = client.session.save()
                with open(f"sessions/{tdata}.session", "w") as file:
                    file.write(auth_key)
                    await client.disconnect()
                    logger.success(f"{tdata} — сохранён.")
                    
        zzz = os.listdir("tdatas")
        nn = len(zzz)
        os.system(f"rm -r tdatas/* ")

    await message.answer(f"<b>Готово ! Акаунты добавленны +{s} шт !</b>", reply_markup=back_to_main_menu)
# 
    await state.finish()
    sessions.clear()

@dp.callback_query_handler(text="sms", state="*")
async def sms(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("💬    <b>Введи текст для рассылки</b>",
                                 reply_markup=back_to_main_menu)
    await sms2.sms_text.set()
    #await call.message.answer('💬     <b>Текст успешно сохранен</b> !',
     #                     reply_markup=back_to_main_menu)
#
    @dp.message_handler(state=sms2.sms_text)
    async def sms_spam(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open('sms.txt', 'w', encoding="utf-8") as f:
            f.write(sms)
        await message.answer('💬     <b>Текст успешно сохранен</b> !',
                            reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="give_time")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>🆔    Введите ID человека:</b>",
                                               reply_markup=back_admin)
    await GiveTime.GT1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=GiveTime.GT1)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    user_id = message.text
    await message.delete()
    await GiveTime.next()
    await state.update_data(user_id=user_id)
    await msg_to_edit.edit_text("<b>⏰  Введите время в часах которое выдать человеку:</b>", reply_markup=back_admin)


@dp.message_handler(state=GiveTime.GT2)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, user_id = data.get("msg_to_edit"), data.get("user_id")
    try:
        hours = int(message.text)
        await message.delete()
        date_when_expires = datetime.now() + timedelta(hours=hours)
        date_to_db = str(date_when_expires).split(".")[0].replace("-", " ").split(":")
        date_to_db = " ".join(date_to_db[:-1])
        await update_date(user_id, date_to_db)
        await state.finish()
        await msg_to_edit.edit_text("<b>Доступ выдан.</b>", reply_markup=back_admin)
    except ValueError:
        await msg_to_edit.edit_text("<b>    ⏰Не верный формат, попробуйте еще раз.</b>")


@dp.callback_query_handler(text="take_time")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>🆔    Введите ID человека:</b>",
                                               reply_markup=back_admin)
    await TakeTime.T1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=TakeTime.T1)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    user_id = message.text
    await message.delete()
    await update_date(user_id, None)
    await state.finish()
    await msg_to_edit.edit_text("<b>У юзера больше нет доступа.</b>", reply_markup=back_admin)


# ========================BROADCAST========================
# ASK FOR PHOTO AND TEXT
@dp.callback_query_handler(text="broadcast")
async def broadcast2(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("🏞    <b>Отправь фото  которое будут рассылаться по юзерам</b>", reply_markup=back_to_main_menu)
    await BroadcastState.BS1.set()


# RECEIVE PHOTO OR TEXT
@dp.message_handler(content_types=['photo'], state=BroadcastState.BS1)
async def broadcast4(message: Message, state: FSMContext):
    await message.delete()
    easy_chars = 'abcdefghijklnopqrstuvwxyz1234567890'
    name = 'cicada'
    photo_name = name + ".jpg"
    await message.photo[-1].download(f"pics/broadcast/{photo_name}")
    await state.update_data(photo=photo_name, text=message.caption)
    with open("foto.txt", "w") as f:
        f.write("+++")
    await asyncio.sleep(2)
    await message.answer("🏞    <b>Фото успешно загруженно</b>", reply_markup=back_to_main_menu)



@dp.callback_query_handler(text="fdel")
async def fdel(call: CallbackQuery):
    try:
        with open("foto.txt", "w") as f:
            f.write("---")
        await call.message.answer("<b>Фото Удаленно</b>", reply_markup=back_to_main_menu)
    except:
        await call.message.answer("<b>Фото Удаленно</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="hahah")
async def broadcast_text_post(call: CallbackQuery):
    try:
        kart = os.listdir("pics/broadcast")
        if kart[0] == 'cicada.jpg':
            path = f'pics/broadcast/cicada.jpg'
            with open(path, 'rb') as f:
                photo = f.read()
            ssm = open('sms.txt', 'r', encoding="utf-8").read()
            zz = ssm.split('|')
            sms = random.choice(zz)
            await call.message.answer_photo(photo=photo, caption=f"{ssm}\n\n"
                                                            f"<b>Все правильно? Отправляем?</b>",
                                    reply_markup=choose_menu)
    except:
        ssm = open('sms.txt', 'r', encoding="utf-8").read()
        zz = ssm.split('|')
        sms = random.choice(zz)
        await call.message.answer(ssm + "\n\n<b>Все правильно? Отправляем?</b>", reply_markup=choose_menu)

from telethon import TelegramClient, sync

@dp.callback_query_handler(text="invait")
async def gru(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Выбери куда добавлять пользователей</b>", reply_markup=inv)



@dp.callback_query_handler(text="invait_can", state="*")
async def canal(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи ссылку группы в таком формате: http://t.me/username/</b>", reply_markup=back_to_main_menu)
    await sms4.sms_text.set()


@dp.message_handler(state=sms4.sms_text)
async def cann(message: Message, state: FSMContext):
    channel = message.text
    msms = await message.answer("<b>Запуск Инвайта</b>")
    ti = open('time.txt', 'r').read()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    if z <= 1:
        await message.answer("Добать получателей список пуст !")
        
    count = int(z)
    i = 0
    d = 0
    s = 0
    c = 0
    o = 0
    ss = os.listdir('sessions')
    mom = len(ss)
    a = 0
    v = 0
    while i <= xx:
        try:
            if mom <= 0:
                break
            if v == z:
                break
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            akk = acaunt.split(".")[0]
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            result = await client(functions.users.GetFullUserRequest(id="me"))
            nam = result.user.first_name
            lnam = result.user.last_name
            if mm <= 20:
                
                try:
                    await client(JoinChannelRequest(channel))
                    o = o + 1
                    mom = mom - 1
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Добавлен пользователь {akk} в группу ✅</b>\n\n"
                        f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti)
                    msm = msm + 1
                    mm = mm + 1
                    v = v + 1
                    
                   
                    d = d + 1
                except:
                    
                    mom = mom - 1
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Не Добавлен {akk} в группу ❌</b>\n\n"
                        f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti/2)
                    d = d + 1
                    v = v + 1
        except:
            i = i + 1
    await message.answer("<b>Инвайт завершил работу</b>", reply_markup=back_to_main_menu)
    await state.finish()


@dp.callback_query_handler(text="ppr", state="*")
async def gru(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи ссылку группы в таком формате: http://t.me/username/</b>", reply_markup=back_to_main_menu)
    await sms5.sms_text.set()



@dp.message_handler(state=sms3.sms_text)
async def gruuu(message: Message, state: FSMContext):
    channel = message.text
    msms = await message.answer("<b>Начинаю Инвайт Группы</b>")
    await message.delete()
    ti = open('time.txt', 'r').read()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    if z <= 1:
        await message.answer("Добать получателей список пуст !")
        
    count = int(z)
    i = 1
    d = 0
    ss = open('ussers.txt', 'r').readlines()
    mom = len(ss)
    c = 0
    o = 0
    msm = 0
    a = 0
    v = 0
    while i <= xx:
        try:
            if mom <= 0:
                break
            if d == 15:
                i = i + 1
            if v == z:
                break
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            await client(JoinChannelRequest(channel))

            if mm <= 20:
                ss = open('ussers.txt', 'r').readlines()
                user = ss[a][:-1]
                akk = acaunt.split(".")[0]
                #await client(functions.channels.InviteToChannelRequest(channel=channel, users = [user]))
                try:
                    await client(InviteToChannelRequest(channel=channel, users = [user]))
                    o = o + 1
                    mom = mom - 1
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Добавлен пользователь {user} в группу ✅</b>\n\n"
                        f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti)
                    mm = mm + 1
                    v = v + 1
                    a = a + 1
                    d = d + 1
                    
                except:
                    mom = mom - 1
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Не Добавлен {user} в группу ❌</b>\n\n"
                        f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti/2)
               #     except:
               #     time.sleep(ti/2)
               #     await message.answer(f"<b>Не вышло добавить пользователь {user} в группу ❌</b>")
               #     d = d + 1
                    a = a + 1
               #     v = v + 1
        except:
          ##  print("ne policilos")
            i = i + 1
            
    await message.answer("<b>Инвайт завершил работу</b>", reply_markup=back_to_main_menu)
    await state.finish()
ban = []
@dp.callback_query_handler(text="invait_grup", state="*")
async def gru(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи ссылку группы в таком формате: http://t.me/username/</b>", reply_markup=back_to_main_menu)
    await sms3.sms_text.set()

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.channels import LeaveChannelRequest
@dp.message_handler(state=sms5.sms_text)
async def gruuu(message: Message, state: FSMContext):
    ch = message.text
    await message.answer("<b>Начинаю парсинг.....</b>")
    ti = open('time.txt', 'r').read()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    file_list = os.listdir('sessions')
    sht = len(file_list)
    xaka = random.randint(0, sht)
    acaunt = file_list[3]
    cli = open(f"sessions/{acaunt}").read()
    client = TelegramClient(StringSession(cli), api_id, api_hash)
    await client.connect()
  
    await client(JoinChannelRequest(ch))
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
    offset_user = 0  
    limit_user = 1000 

    all_participants = []   # список всех участников канала
    filter_user = ChannelParticipantsSearch('')

    participants = await client(GetParticipantsRequest(ch,
        filter_user, offset_user, limit_user, hash=0))

    all_participants.extend(participants.users)
    offset_user += len(participants.users) # len(participants.users)
    await message.answer("<b>Идет сохранения списка.....</b>")
    all_users_details = []   # список словарей с интересующими параметрами участников канала
    for participant in all_participants:
        dd = participant.status

        if  not participant.username == None:
            all_users_details.append(participant.username)   


    for x in all_users_details:
        ss = x
        if not ss[-3:] == "bot":
            with open("ussers.txt", "a") as f:
                f.write(str(f"{x}\n"))
    zx = len(open('ussers.txt', 'r').readlines())
    await client(LeaveChannelRequest(ch))
    await message.answer(
        f"<b>Список сохранен</b>\n"
        f"<b>Получено {zx} пользователей</b>", reply_markup=back_to_main_menu)

async def sending_check(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        nv2 = (datetime.now().strftime("%d %B, %Y"))
        nv = (datetime.now().strftime("%H:%M:%S"))
        print(nv2)
        if nv[:7] == "12:00:0":
            print(nv2)
            #with open(f"{username}.db", "rb") as doc:
                #await bot.send_document(692916588,
                                       ## doc,
                                       # caption=f"📦 BACKUP\n"
                                        #        f"🕜 {tt}")

            time.sleep(2)
vv = int('6')
async def on_startup2(vv):
    while True:
        await asyncio.sleep(vv)
        nv2 = (datetime.now().strftime("%d %b %Y, %H:%M"))
        nv = (datetime.now().strftime("%H:%M:%S"))
        off_spam = open("spam/spam.txt", "r", encoding="utf-8").readlines()

                        
        for x in off_spam:
            offs = x.split()
            voz = offs[0]
            vz = voz.split("'")
            wernyt = vz[1]
            pr = f"{offs[2]} {offs[3]} {offs[4]} {offs[5]}"
            if pr == nv2:
                shutil.move(f"spam/{wernyt}", f"sessions/{wernyt}")
                with open("spam/spam.txt", "w", encoding="utf-8") as f:
                    f.writelines(off_spam[1:])
        
       # if nv[:7] == "12:00:0":
       #     print(nv2)
       #     time.sleep(5)
        
"""
    @dp.callback_query_handler(text="stop_spam")
    async def st(call: CallbackQuery):
        with open("stop.txt", "w") as f:
            f.write("1")

    tmr = Timer(1.0, start_clock)
    tmr.start()
    """


@dp.callback_query_handler(text="stop_spam")
async def st(call: CallbackQuery):
    with open("stop.txt", "w") as f:
        f.write("1")

# START BROADCAST
@dp.callback_query_handler(text="go_start")
async def broadcast_text_post(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    ded = await call.message.answer("<b>Спам Рассылка Запущенна !</b>")
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    mom = len(ss)
    open("otcet.txt", "w", encoding="utf-8")
    with open("stop.txt", "w") as f:
        f.write("0")
    i = 0
    p = 0
    t = 0
    c = 0
    o = 0
    propusk = 0

    while xx >= i:
        acaunt = file_list[i]
        try:
            npn  = int(open(f"{acaunt}.txt", "r").read())
        except:
            i = i + 1
            continue
        print(npn)
        if npn <= 0:
            i = i + 1
            continue
        akk = acaunt.split(".")[0]
        ti = int(open('time.txt', 'r').read())
        sto = int(open('stop.txt', 'r').read())
        if sto == 1:
            
            break
        try:
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
        except:
            client = TelegramClient(f"sessions/{acaunt}", api_id, api_hash)
            await client.connect()

        fff = open("pics/broadcast/cicada.jpg", 'rb').read() 
        ssm = open('sms.txt', 'r', encoding="UTF-8").read()
        zz = ssm.split('|')
        sms = random.choice(zz)
        try:
          file_list2 = open('ussers.txt', 'r').readlines()
        except:
          await call.message.answer("Рассылка завершена", reply_markup=back_to_main_menu)
            

        if propusk == 3:
            #await client.disconnect()
            i = i + 1
            t = t - 9
            propusk = 0
        if mom <= 0:
            break

        if p >= 3:
            ban.append(acaunt)
            #await client.disconnect()
            i = i + 1
            p = p - 40
        if len(file_list2) >= p:
            try:
                ft = open("foto.txt", "r").read()
                if ft == "+++":
                    with open("ussers.txt", "r") as z:
                        lines = z.readlines()
                        far = lines[0][:-1]
                    xxw = await client.get_entity(far)
                    
                    if xxw.first_name:
                        await client.send_file(far, file=fff, caption=ssm)
                        with open("ussers.txt", "w") as f:
                            f.writelines(lines[1:])
                if ft == "---":

                    with open("ussers.txt", "r") as z:
                        lines = z.readlines()
                        far = lines[0][:-1]
                    xxw = await client.get_entity(far)
                    if xxw.first_name:
                        #await call.message.answer(xxw.first_name)
                        await client.send_message(far, ssm)
                        with open("ussers.txt", "w") as f:
                            f.writelines(lines[1:])
                p = p + 1
                propusk = 0
                t = t + 1
                o = o + 1
                result = await client(functions.users.GetFullUserRequest(id="me"))
                nam = result.user.first_name
                lnam = result.user.last_name
                
                try:
                    xxx = file_list2[t][:-1]
                except:
                    pass
                await ded.edit_text(
                            f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {akk} 💠 {nam} {lnam} ⚜️</b>\n\n"
                            f"<b>На пользователя 🗣 {far} ✅</b>\n\n"
                            f"🛑    <b>Пауза между смс:</b>   <b>{ti} сек</b>\n"
                            f"<b>❌     Недоставленно:  {c}</b>\n"
                            f"<b>✅     Доставленно:    {o}</b>\n\n"
                            f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                mom = mom - 1
                npn  = int(open(f"{acaunt}.txt", "r").read())
                zczc = int(npn - 1)
                print(zczc)
                with open(f"{acaunt}.txt", "w") as m:
                    m.write(zczc)
                otc = """✉️    Рассылка с Акаунта:    \n\n    ⚜️ {akk} 💠 {nam} {lnam} ⚜️
                            На пользователя 🗣 {far} ✅
                            🛑    Пауза между смс:   {ti} 
                            ❌     Недоставленно:  {c}
                            ✅     Доставленно:    {o}
                            ‼️ Осталось 👩‍👩‍👧‍👧 {mom}"""
                

                with open("otcet.txt", "a", encoding="utf-8") as f:
                    f.write(str(f"{otc}\n"))
                time.sleep(ti)
            except:
                p = p + 1
                t = t + 1
                c = c + 1
                result = await client(functions.users.GetFullUserRequest(id="me"))
                nam = result.user.first_name
                lnam = result.user.last_name
                try:
                    xxx = file_list2[t][:-1]
                except:
                    pass
                await ded.edit_text(
                            f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {akk} 💠 {nam} {lnam} ⚜️</b>\n\n"
                            f"<b>На пользователя 🗣 {far} ❌</b>\n\n"
                            f"🛑    <b>Пауза между смс:</b>   <b>{ti} сек</b>\n"
                            f"<b>❌     Недоставленно:  {c}</b>\n"
                            f"<b>✅     Доставленно:    {o}</b>\n\n"
                            f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                with open("ussers.txt", "w") as f:
                    f.writelines(lines[1:])
                time.sleep(ti/2)
                propusk = propusk + 1
                mom = mom - 1
                await client.disconnect()
        else:
            await client.disconnect()
            i = i + 1
            mom = mom - 1
    sto = int(open('stop.txt', 'r').read())
    if sto == 1:
        await call.message.answer("Рассылка остановлена", reply_markup=back_to_main_menu)
    else:
        await call.message.answer("✅ <b>Рассылка Завершена</b> ✅", reply_markup=back_to_main_menu)    

        

ydalen = []

@dp.callback_query_handler(text="ceker")
async def broadcast_text_post(call: CallbackQuery, state: FSMContext):
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581" 
    file_list = os.listdir('sessions')
    xx = len(file_list)   
    i = 0
    s = 0
    sp = 0
    tit = 0 
    r = 1
    while i <= xx:
        try:
            mm = 0         
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            i = i + 1
            

            channel_username = "SpamBot"
            gg = await client.send_message(channel_username, "/start")
            kk = gg.peer_id.user_id
            posts = await client.get_messages(
                    gg.peer_id.user_id
                    )
            
            for x in posts:
                fff = x.message

                if fff == 'Good news, no limits are currently applied to your account. You’re free as a bird!':
                    await call.message.edit_text(
                        f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
                        f"❌    <b>В Спаме:  {sp}</b>\n"
                        f"❌❌❌   <b>Мертвые:  {tit}</b>\n"
                        f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                        f"<b>Акаунт \n💠 {acaunt.split('.')[0]}💠 </b> ✅\n"
                        #f"Доступно смс на сегодня: {tete}\n\n"
                        f"<b>SpamBot:  {fff[10:20]}</b>")
                    r = r + 1
                    time.sleep(2)
                    await client.disconnect()  
                    break
                if not fff == 'Good news, no limits are currently applied to your account. You’re free as a bird!':
                    with open("spam.txt", "w", encoding="utf-8") as f:
                            f.write(str(fff))
                    ssppam = open("spam.txt", "r", encoding="utf-8").readlines()
                    spm = ssppam[1].split("until")
                    await call.message.edit_text(
                            f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
                            f"❌    <b>В Спаме:  {sp}</b>\n"
                            f"❌❌❌   <b>Мертвые:  {tit}</b>\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f"<b>Акаунт \n💠 {acaunt.split('.')[0]}💠 </b> ❌\n"
                            f"<b>SpamBot:  {spm[1][:-1]}</b>")
                    
                    with open("spam/spam.txt", "a") as ff:
                        ff.write(str(f"{[acaunt, spm[1][:-1]]}\n"))
                    shutil.move(f"sessions/{acaunt}", f"spam/{acaunt}")
                    sp = sp + 1
                    time.sleep(2)
                    await client.disconnect()  
                    break
                
        except:
            time.sleep(2)
            ydalen.append(acaunt)
            tit = len(ydalen)      
            await client.disconnect()  
            i = i + 1 
        break 
    keyboard = InlineKeyboardMarkup()
    for x in ydalen:
        keyboard.add(InlineKeyboardButton(text=x.split('.')[0], callback_data=x))
    keyboard.add(InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu"))

    await call.message.answer(
                            f"🔍    <b>Проверка Завершена</b> !\n\n"
                            f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
                            f"❌    <b>В Спаме:  {sp}</b>\n"
                            f"❌❌❌   <b>Мертвые:  {tit}</b>\n") 
    await call.message.answer('<b>Какой Акаунт Удалить ?</b>\n\n', reply_markup=keyboard)
    @dp.callback_query_handler(lambda c: c.data)
    async def poc_callback_but(c:CallbackQuery):
        ydal = c.data
        os.remove(f"sessions/{ydal}")
        await call.message.answer(f'<b>✅ Акаунт {ydal.split(".")[0]} Удален ✅</b>', reply_markup=back_to_main_menu)

@dp.callback_query_handler(text="xxx")
async def exitt(call: CallbackQuery):
    await call.message.edit_text("<b>меню</b>", reply_markup=back_to_main_menu)
