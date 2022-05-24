from typing import List, Any
from asgiref.sync import sync_to_async
from backend.models import *


@sync_to_async
def add_kesh(kod, summa):
    try:
        return Kashlar(kod=kod, summa=summa).save()
    except Exception as err:
        print(err)


@sync_to_async
def add_ishlatilgan(kod, summa, user_id):
    try:
        return Ishlatilgan(kod=kod, summa=summa, user_id=user_id).save()
    except Exception as err:
        print(err)


@sync_to_async
def get_ishlatilgan(kod):
    try:
        category = Ishlatilgan.objects.filter(kod=kod).first()
        return category
    except:
        return None


@sync_to_async
def get_kesh(kod):
    try:
        category = Kashlar.objects.filter(kod=kod).first()
        return category
    except:
        return None


@sync_to_async
def get_by_id(user_id):
    try:
        category = Ishlatilgan.objects.filter(user_id=user_id)
        return category
    except:
        return None
