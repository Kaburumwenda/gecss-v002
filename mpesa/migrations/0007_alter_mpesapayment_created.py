# Generated by Django 4.0.8 on 2022-11-17 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0006_mpesapay_alter_mpesapayment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesapayment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 17, 14, 26, 52, 791262)),
        ),
    ]
