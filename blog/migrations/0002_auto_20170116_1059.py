# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['post_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment_date']},
        ),
    ]
