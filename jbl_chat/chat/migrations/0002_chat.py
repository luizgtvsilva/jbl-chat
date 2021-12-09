# Generated by Django 3.2.9 on 2021-12-08 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('from_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='chat.user')),
                ('to_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='chat.user')),
            ],
            options={
                'db_table': 'chat',
            },
        ),
    ]
