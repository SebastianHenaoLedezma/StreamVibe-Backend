# Generated by Django 5.0.4 on 2024-05-15 23:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0026_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='review',
        ),
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.ManyToManyField(default=[], to='be_streamvibe.rating'),
        ),
        migrations.AddField(
            model_name='movie',
            name='reviews',
            field=models.ManyToManyField(default=[], to='be_streamvibe.review'),
        ),
        migrations.AddField(
            model_name='review',
            name='ratings',
            field=models.ManyToManyField(to='be_streamvibe.rating'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_url',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='video'),
        ),
    ]