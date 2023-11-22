# Generated by Django 4.2.6 on 2023-11-22 07:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=8, message='密码长度不能少于10个字符')], verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='邮箱'),
        ),
    ]
