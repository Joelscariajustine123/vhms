# Generated by Django 4.2 on 2023-06-26 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vhmsapp', '0010_alter_admission_options_admission_admitedby_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.doctor'),
        ),
    ]
