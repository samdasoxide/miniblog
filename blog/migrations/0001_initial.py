# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 22:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of blog author', max_length=200)),
                ('bio', models.TextField(help_text="Enter some of author's biography")),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter blog title', max_length=200)),
                ('post_date', models.DateField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular comment', primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Blog')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
