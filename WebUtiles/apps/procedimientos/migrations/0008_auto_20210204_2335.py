# Generated by Django 3.1.5 on 2021-02-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedimientos', '0007_auto_20210125_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]