from django.db import models


class Kashlar(models.Model):
    kod = models.CharField(max_length=12, primary_key=True)
    summa = models.PositiveIntegerField(default=0)


class Ishlatilgan(models.Model):
    kod = models.CharField(max_length=12, primary_key=True)
    summa = models.PositiveIntegerField(default=0)
    user_id = models.CharField(max_length=25, null=True, blank=True)


class DoctorPay(models.Model):
    user_id = models.CharField(unique=True, max_length=25)
    summa = models.PositiveIntegerField(default=0)
    name = models.CharField(null=True, blank=True, max_length=125)
