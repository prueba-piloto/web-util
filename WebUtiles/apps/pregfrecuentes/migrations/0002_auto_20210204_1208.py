# Generated by Django 3.1.5 on 2021-02-04 15:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pregfrecuentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frecuentes',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
