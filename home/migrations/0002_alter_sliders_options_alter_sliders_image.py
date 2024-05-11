# Generated by Django 5.0.6 on 2024-05-11 21:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sliders',
            options={'verbose_name_plural': 'Slider Section'},
        ),
        migrations.AlterField(
            model_name='sliders',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
