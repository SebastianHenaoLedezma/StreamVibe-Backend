# Generated by Django 5.0.4 on 2024-05-07 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
