# Generated by Django 3.2.3 on 2021-06-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=7)),
                ('text', models.TextField()),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MapSession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('bdate', models.CharField(max_length=10)),
                ('btime', models.CharField(max_length=5)),
                ('bplace', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=6)),
                ('user', models.CharField(default='', max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('Su', models.CharField(max_length=15)),
                ('Mo', models.CharField(max_length=15)),
                ('Me', models.CharField(max_length=15)),
                ('Ma', models.CharField(max_length=15)),
                ('Ju', models.CharField(max_length=15)),
                ('Ve', models.CharField(max_length=15)),
                ('Sa', models.CharField(max_length=15)),
                ('Ra', models.CharField(max_length=15)),
                ('Ke', models.CharField(max_length=15)),
                ('As', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserVideoLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
            ],
        ),
    ]