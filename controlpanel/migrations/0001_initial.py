# Generated by Django 3.2.7 on 2021-10-04 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateLisDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datelis', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='divisionName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MultiDateLisDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datelis', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='PlanetChanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planetName', models.CharField(max_length=100)),
                ('planetChangedName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrendCharts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('cName', models.CharField(max_length=100)),
                ('cPlace', models.CharField(max_length=100)),
                ('cDate', models.CharField(max_length=100)),
                ('cTime', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='modelNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelFullName', models.CharField(max_length=100)),
                ('birthDateTime', models.CharField(max_length=100)),
                ('modelLocation', models.CharField(max_length=100)),
                ('modelcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlpanel.divisionname')),
            ],
        ),
    ]
