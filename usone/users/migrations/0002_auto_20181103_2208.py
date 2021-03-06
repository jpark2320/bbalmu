# Generated by Django 2.0.9 on 2018-11-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('georgia', 'Georgia'), ('new_york', 'New York'), ('los_angeles', 'Los Angeles'), ('san_francisco', 'San Francisco')], default='georgia', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
