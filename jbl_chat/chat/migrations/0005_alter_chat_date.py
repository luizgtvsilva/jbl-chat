# Generated by Django 3.2.9 on 2021-12-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_chat_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(verbose_name='08/12/2021 22:33:52'),
        ),
    ]
