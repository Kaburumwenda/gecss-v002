# Generated by Django 4.0.8 on 2022-11-18 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0008_alter_mpesapayment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesapayment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 18, 10, 52, 0, 154752)),
        ),
    ]
