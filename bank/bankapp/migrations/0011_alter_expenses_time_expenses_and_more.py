# Generated by Django 4.1.2 on 2022-11-07 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0010_alter_expenses_sum_alter_expenses_time_expenses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='time_expenses',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 17, 49, 44, 880221)),
        ),
        migrations.AlterField(
            model_name='savings',
            name='time_saving',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 17, 49, 44, 880221)),
        ),
    ]