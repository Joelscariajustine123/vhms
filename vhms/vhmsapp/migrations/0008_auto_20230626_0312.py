# Generated by Django 3.1.2 on 2023-06-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhmsapp', '0007_auto_20230626_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/pet_images/'),
        ),
    ]