# Generated by Django 3.1.5 on 2021-01-27 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebUtil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=300)),
                ('slug', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]