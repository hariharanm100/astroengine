# Generated by Django 3.2.2 on 2023-11-17 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persontoperson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthchartdb',
            name='user',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
