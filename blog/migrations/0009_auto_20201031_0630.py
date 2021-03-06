# Generated by Django 3.1 on 2020-10-31 06:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_interval_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='interval_length',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=9, message='9'), django.core.validators.MaxLengthValidator(limit_value=42, message='42')], verbose_name='interval length'),
        ),
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.DecimalField(decimal_places=3, max_digits=9, null=True, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)], verbose_name='number'),
        ),
        migrations.AlterField(
            model_name='post',
            name='interval_value',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(limit_value=42, message='Не более 42'), django.core.validators.MinValueValidator(limit_value=9, message='Не менее 9')], verbose_name='interval'),
        ),
    ]
