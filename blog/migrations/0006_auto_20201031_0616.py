# Generated by Django 3.1 on 2020-10-31 06:16

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='int_list_comma',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='list comma'),
        ),
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.validate_ipv46_address], verbose_name='ip'),
        ),
    ]
