# Generated by Django 3.2 on 2021-07-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SitePrimebot', '0003_auto_20210720_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='estrategia',
            name='apm',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='estrategia',
            name='escanteios',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='estrategia',
            name='gols',
            field=models.IntegerField(null=True),
        ),
    ]
