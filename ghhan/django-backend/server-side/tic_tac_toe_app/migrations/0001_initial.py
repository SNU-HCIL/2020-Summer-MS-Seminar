# Generated by Django 3.1 on 2020-08-04 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_date', models.DateTimeField(verbose_name='time created')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_text', models.CharField(max_length=4)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tic_tac_toe_app.game')),
            ],
        ),
    ]