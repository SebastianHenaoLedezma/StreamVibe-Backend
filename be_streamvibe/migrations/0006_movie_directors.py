# Generated by Django 5.0.4 on 2024-05-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0005_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(to='be_streamvibe.director'),
        ),
    ]
