# Generated by Django 3.1.5 on 2021-07-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorized_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='HH',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='IH',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='JH',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='SSH',
            field=models.BooleanField(default=False),
        ),
    ]
