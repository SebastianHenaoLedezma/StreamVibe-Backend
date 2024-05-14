# Generated by Django 4.2.13 on 2024-05-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0011_movie_actors'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=50)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]