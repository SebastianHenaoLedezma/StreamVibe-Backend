# Generated by Django 4.2.13 on 2024-05-13 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0013_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(max_length=250),
        ),
        migrations.CreateModel(
            name='Support_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.IntegerField(default=0)),
                ('messages', models.TextField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='be_streamvibe.user')),
            ],
        ),
    ]
