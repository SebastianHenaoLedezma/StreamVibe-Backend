# Generated by Django 5.0.4 on 2024-05-14 23:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0022_alter_actor_photo_url_alter_director_photo_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_url',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='video'),
        ),
    ]
