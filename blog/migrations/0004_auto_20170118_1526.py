# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170118_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='', help_text='Enter name of blog author', max_length=200),
            preserve_default=False,
        ),
    ]
