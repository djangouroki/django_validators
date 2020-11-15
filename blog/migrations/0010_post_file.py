# Generated by Django 3.1 on 2020-10-31 08:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201031_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(null=True, upload_to='file/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xlsx', 'jpg'], message='Не тот файл!')], verbose_name='file'),
        ),
    ]