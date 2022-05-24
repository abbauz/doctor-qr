import datetime
from itertools import product

from aiogram import types
import pandas as pd
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from utils.db_api import database as commands
from loader import dp, bot
from keyboards.inline.menu_button import doctor_menu, confirm_keyboard, get_or_back, back_to, year_keyboard, \
    month_keyboard
from keyboards.inline.main_inline import admin_menu, back_admin_menu, doctor_in_admin, category_keyboard
from utils.db_api.database import *

