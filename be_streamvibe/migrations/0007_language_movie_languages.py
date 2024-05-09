# Generated by Django 5.0.4 on 2024-05-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0006_movie_directors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='languages',
            field=models.ManyToManyField(to='be_streamvibe.language'),
        ),
    ]