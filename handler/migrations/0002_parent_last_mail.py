# Generated by Django 3.0.7 on 2020-08-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='last_mail',
            field=models.DateField(blank=True, null=True),
        ),
    ]
