# Generated by Django 3.0.7 on 2020-07-12 22:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0009_auto_20200713_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 22, 33, 17, 938009, tzinfo=utc)),
        ),
    ]
