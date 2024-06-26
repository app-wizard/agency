# Generated by Django 5.0.6 on 2024-05-12 11:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('button_text', models.CharField(blank=True, max_length=300, null=True)),
                ('button_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('top', models.BooleanField(default=False)),
                ('top_text', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
