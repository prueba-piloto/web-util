# Generated by Django 3.1.5 on 2021-01-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedimientos', '0004_auto_20210121_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]