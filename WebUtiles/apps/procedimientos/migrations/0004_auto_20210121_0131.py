# Generated by Django 3.1.5 on 2021-01-21 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedimientos', '0003_auto_20210121_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, default='static/img/proced.jpg', upload_to='static'),
        ),
    ]