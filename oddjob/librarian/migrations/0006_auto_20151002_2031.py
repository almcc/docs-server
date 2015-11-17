# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0005_auto_20151002_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='release',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='artifact',
            unique_together=set([('name', 'release')]),
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('name', 'product')]),
        ),
    ]
