# Generated by Django 3.1.5 on 2021-07-04 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fitness_analyser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ED',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ED_count', models.PositiveSmallIntegerField(default=0)),
                ('cn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fitness_analyser.cadet_bio')),
            ],
        ),
    ]
