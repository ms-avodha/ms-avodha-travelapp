# Generated by Django 3.1.4 on 2021-01-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_news_minidesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='month',
            field=models.CharField(max_length=10),
        ),
    ]
