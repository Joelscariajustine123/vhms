# Generated by Django 4.2 on 2023-06-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhmsapp', '0002_remove_doctor_department_doctor_departments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='animalname',
        ),
        migrations.AddField(
            model_name='animal',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Animal '),
        ),
    ]
