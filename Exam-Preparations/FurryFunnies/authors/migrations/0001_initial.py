# Generated by Django 5.0.4 on 2024-10-27 07:30

import authors.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4), authors.validators.ContainsOnlyLettersValidator()])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), authors.validators.ContainsOnlyLettersValidator()])),
                ('passcode', models.CharField(help_text='Your passcode must be a combination of 6 digits', max_length=6, validators=[authors.validators.HasExactlySixDigitsValidator()])),
                ('pets_number', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('info', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
