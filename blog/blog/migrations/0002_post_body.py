# Generated by Django 3.0.1 on 2023-06-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='qqq'),
        ),
    ]
