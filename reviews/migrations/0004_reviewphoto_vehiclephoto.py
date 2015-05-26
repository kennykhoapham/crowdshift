# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_profilephoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.FileField(upload_to=b'review-photos')),
                ('review', models.ForeignKey(to='reviews.Review')),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.FileField(upload_to=b'vehicle-photos')),
                ('vehicle', models.ForeignKey(to='reviews.Vehicle')),
            ],
        ),
    ]
