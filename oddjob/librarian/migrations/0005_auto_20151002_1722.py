# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0004_auto_20151002_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='release',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
