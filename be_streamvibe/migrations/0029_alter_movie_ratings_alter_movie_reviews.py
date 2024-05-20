# Generated by Django 5.0.4 on 2024-05-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0028_alter_movie_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='ratings',
            field=models.ManyToManyField(default=[], null=True, to='be_streamvibe.rating'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='reviews',
            field=models.ManyToManyField(default=[], null=True, to='be_streamvibe.review'),
        ),
    ]