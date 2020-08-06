# Generated by Django 3.1 on 2020-08-06 03:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tic_tac_toe_app', '0002_auto_20200806_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='time ended'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='start_date',
            field=models.DateTimeField(verbose_name='time started'),
        ),
    ]
