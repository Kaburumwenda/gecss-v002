# Generated by Django 4.0.5 on 2022-07-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0007_batteryswap_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='batteryswap',
            name='source',
            field=models.CharField(default='Online', max_length=150),
        ),
    ]
