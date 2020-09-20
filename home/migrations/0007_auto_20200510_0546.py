# Generated by Django 3.1.dev20200327073858 on 2020-05-10 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200506_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contactformmessage',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='contactformmessage',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
