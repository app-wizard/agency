# Generated by Django 5.0.6 on 2024-05-11 23:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_about_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image2'),
        ),
    ]