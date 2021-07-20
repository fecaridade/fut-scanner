# Generated by Django 3.2 on 2021-07-20 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SitePrimebot', '0002_estrategia_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='estrategia',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='telegramUser',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='estrategia',
            name='nome',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegramID',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterOrderWithRespectTo(
            name='estrategia',
            order_with_respect_to='user',
        ),
    ]
