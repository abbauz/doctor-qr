from aiogram import types
from loader import dp
from keyboards.inline.menu_button import get_my_money
import pandas as pd
from utils.db_api.database import *
from aiogram.utils.deep_linking import decode_payload, get_start_link
import pyqrcode
import qrcode

Api_key = '2X4-oB_kOf9loP-UV92I64iWdDNK2Aa_ks0rFDrLDpxjY_ziRHhJvq_xbaAXH6c-'


@dp.message_handler(commands=["start"])
async def handler(message: types.Message):
    args = message.get_args()
    payload = decode_payload(args)
    if payload != '':
        kod = await get_ishlatilgan(payload)
        if kod is None:
            pay = await get_kesh(payload)
            markup = await get_my_money()
            await message.answer(f"Keshbek qabul qilindi", reply_markup=markup)
            await add_ishlatilgan(user_id=message.from_user.id, kod=payload, summa=pay.summa)
        else:
            markup = await get_my_money()
            await message.answer('Bu kod oldin ishlatilgan', reply_markup=markup)
    else:
        await message.answer(f'Fayl yuklang')


@dp.message_handler(lambda message: message.text in ['Barcha keshbeklar'])
async def get_money(message: types.Message):
    user_id = message.from_user.id
    useer = await get_by_id(user_id)
    all = 0
    for i in useer:
        all += i.summa
    await message.answer(text=f'Umumiy kesh bek: {all}')


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def add_kash(message: types.Message):
    await message.document.download('new_file.xlsx')
    df = pd.read_excel('new_file.xlsx')
    for i in df.index:
        kod = df['kash'][i]
        pay = await get_kesh(kod)
        if pay is None:
            await add_kesh(kod=df['kash'][i], summa=df['summa'][i])
            link = await get_start_link(f'{kod}', encode=True)
            q = qrcode.make(f'{link}')
            q.save('qrcode.png')
            photo = open('qrcode.png', 'rb')
            await message.answer_photo(caption=link, photo=photo)
