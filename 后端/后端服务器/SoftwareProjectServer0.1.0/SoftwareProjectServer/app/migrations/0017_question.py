# Generated by Django 4.2.6 on 2023-12-10 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='题干')),
                ('question_picture', models.BinaryField(blank=True, null=True, verbose_name='题目图片')),
                ('option_1', models.CharField(blank=True, max_length=256, null=True, verbose_name='选项1')),
                ('option_2', models.CharField(blank=True, max_length=256, null=True, verbose_name='选项2')),
                ('option_3', models.CharField(blank=True, max_length=256, null=True, verbose_name='选项3')),
                ('option_4', models.CharField(blank=True, max_length=256, null=True, verbose_name='选项4')),
                ('option_5', models.CharField(blank=True, max_length=256, null=True, verbose_name='选项5')),
                ('answer', models.CharField(blank=True, max_length=1, null=True, verbose_name='答案')),
                ('question_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='题型')),
            ],
        ),
    ]
