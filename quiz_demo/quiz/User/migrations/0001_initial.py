# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=200, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(default=b'e10adc3949ba59abbe56e057f20f883e', max_length=200, verbose_name='\u5bc6\u7801')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
