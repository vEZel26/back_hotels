# Generated by Django 4.2.1 on 2023-05-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberreserved',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя забронировшего'),
        ),
        migrations.AlterField(
            model_name='numberreserved',
            name='date_end_reserved',
            field=models.DateField(verbose_name='Дата выезда'),
        ),
        migrations.AlterField(
            model_name='numberreserved',
            name='date_start_reserved',
            field=models.DateField(verbose_name='Дата въезда'),
        ),
        migrations.AlterField(
            model_name='numberreserved',
            name='email_reserved',
            field=models.CharField(max_length=255, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='numberreserved',
            name='phone_reserved',
            field=models.CharField(max_length=255, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='numberreserved',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип номера'),
        ),
    ]
