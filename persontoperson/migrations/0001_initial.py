# Generated by Django 3.2.3 on 2021-06-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='birthchartdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('time_of_birth', models.TimeField()),
                ('place_of_birth', models.CharField(max_length=100)),
                ('coordinates_lan', models.FloatField(blank=True, null=True)),
                ('coordinates_lon', models.FloatField(blank=True, null=True)),
                ('time_zone', models.CharField(blank=True, max_length=100, null=True)),
                ('timeZoneId', models.CharField(blank=True, max_length=100, null=True)),
                ('timeZoneName', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='concatenation_points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_type', models.CharField(max_length=20)),
                ('con_name', models.CharField(max_length=20)),
                ('con_points', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='distance_multiplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('multiplier', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GlobalDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suDegree', models.FloatField()),
                ('moDegree', models.FloatField()),
                ('meDegree', models.FloatField()),
                ('maDegree', models.FloatField()),
                ('juDegree', models.FloatField()),
                ('veDegree', models.FloatField()),
                ('saDegree', models.FloatField()),
                ('raDegree', models.FloatField()),
                ('keDegree', models.FloatField()),
                ('asDegree', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personName', models.CharField(max_length=100)),
                ('suDegree', models.FloatField()),
                ('moDegree', models.FloatField()),
                ('meDegree', models.FloatField()),
                ('maDegree', models.FloatField()),
                ('juDegree', models.FloatField()),
                ('veDegree', models.FloatField()),
                ('saDegree', models.FloatField()),
                ('raDegree', models.FloatField()),
                ('keDegree', models.FloatField()),
                ('asDegree', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='plotimages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_conj', models.ImageField(blank=True, upload_to='')),
                ('img_180', models.ImageField(blank=True, upload_to='')),
                ('img_120l', models.ImageField(blank=True, upload_to='')),
                ('img_120g', models.ImageField(blank=True, upload_to='')),
                ('img_90l', models.ImageField(blank=True, upload_to='')),
                ('img_90g', models.ImageField(blank=True, upload_to='')),
                ('img_60l', models.ImageField(blank=True, upload_to='')),
                ('img_60g', models.ImageField(blank=True, upload_to='')),
                ('img_150', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
