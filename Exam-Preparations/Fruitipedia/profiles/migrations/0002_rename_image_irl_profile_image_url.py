# Generated by Django 5.0.4 on 2024-10-24 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image_irl',
            new_name='image_url',
        ),
    ]
