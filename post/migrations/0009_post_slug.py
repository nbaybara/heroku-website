# Generated by Django 3.1.dev20200327073858 on 2020-05-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20200519_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
    ]
