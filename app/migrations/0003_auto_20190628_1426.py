# Generated by Django 2.0.13 on 2019-06-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190628_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]