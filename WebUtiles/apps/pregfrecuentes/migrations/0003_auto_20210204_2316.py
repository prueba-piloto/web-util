# Generated by Django 3.1.5 on 2021-02-05 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pregfrecuentes', '0002_auto_20210204_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frecuentes',
            name='titulo',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
