# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='review',
            name='vehicle',
            field=models.ForeignKey(to='reviews.Vehicle'),
        ),
    ]
