# Generated by Django 4.2 on 2023-06-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhmsapp', '0005_remove_person_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='animal_images/'),
        ),
    ]
