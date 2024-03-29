# Generated by Django 3.1.5 on 2021-07-04 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadet_Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_N', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=120)),
                ('entry', models.CharField(max_length=20)),
                ('house', models.CharField(max_length=20)),
                ('date_joined', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=120, null=True)),
                ('csv_file', models.FileField(null=True, upload_to='csvs')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('push_ups', models.PositiveSmallIntegerField()),
                ('chin_ups', models.PositiveSmallIntegerField()),
                ('sit_ups', models.PositiveSmallIntegerField()),
                ('One_Mile', models.PositiveSmallIntegerField()),
                ('Two_Miles', models.PositiveSmallIntegerField()),
                ('average', models.FloatField(blank=True)),
                ('PT_Test_Date', models.DateField()),
                ('cn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness_analyser.cadet_bio')),
            ],
        ),
    ]
