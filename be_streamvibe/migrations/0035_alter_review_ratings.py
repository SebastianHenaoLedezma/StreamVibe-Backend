# Generated by Django 5.0.4 on 2024-05-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0034_alter_movie_trailer_thumbnail_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ratings',
            field=models.ManyToManyField(blank=True, default=None, to='be_streamvibe.rating'),
        ),
    ]
