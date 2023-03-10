# Generated by Django 4.0.8 on 2022-11-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentNo', models.CharField(max_length=20)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('fromDate', models.DateField()),
                ('tomDate', models.DateField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Paid', max_length=20)),
            ],
        ),
    ]
