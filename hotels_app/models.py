from django.db import models
from django.contrib.auth.models import AbstractUser
class NumberReserved(models.Model):
    type = models.CharField(max_length=255, null=True, blank=True, verbose_name='Тип номера')
    date_start_reserved = models.DateField(verbose_name='Дата въезда')
    date_end_reserved = models.DateField(verbose_name='Дата выезда')
    email_reserved = models.CharField(max_length=255, verbose_name='Почта')
    phone_reserved = models.CharField(max_length=255, verbose_name='Телефон')
    name = models.CharField(max_length=255,null=True, blank=True, verbose_name='Имя забронировшего')

class WorkingPosition(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Должность')

class UserReserved(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=255, verbose_name='Телефон')

class Number(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    type = models.CharField(max_length=255, verbose_name="Тип номера")
    rooms = models.IntegerField(verbose_name='Количество комнат')

class User(AbstractUser):
    working_position = models.ForeignKey(WorkingPosition, on_delete=models.CASCADE, verbose_name='Должность', related_name='working_position', blank=True, null=True)