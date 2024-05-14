# Generated by Django 4.2.13 on 2024-05-13 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0016_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='be_streamvibe.movie')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='be_streamvibe.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='be_streamvibe.user')),
            ],
        ),
    ]
