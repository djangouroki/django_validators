# Generated by Django 3.1 on 2020-10-31 06:18

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201031_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='int_list_sep',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator(re.compile('^(-)?\\d+(?::(-)?\\d+)*\\Z'), code='invalid', message='Используйте двоетечие!')], verbose_name='list sep'),
        ),
    ]