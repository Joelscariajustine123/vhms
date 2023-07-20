# Generated by Django 4.2 on 2023-06-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhmsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='department',
        ),
        migrations.AddField(
            model_name='doctor',
            name='departments',
            field=models.ManyToManyField(blank=True, to='vhmsapp.department'),
        ),
    ]
