# Generated by Django 3.2.2 on 2021-10-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiples', '0003_model2charts'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendChart4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chartName', models.CharField(max_length=100)),
                ('nameLis', models.CharField(max_length=100)),
                ('combinations', models.CharField(max_length=100)),
                ('data', models.TextField(blank=True, default='{}', null=True)),
            ],
        ),
    ]
