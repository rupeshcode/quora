# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 18:24
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('details', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='answer',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='comment',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Answer'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
