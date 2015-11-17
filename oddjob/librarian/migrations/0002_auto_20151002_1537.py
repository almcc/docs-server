# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ManyToManyField(to='librarian.Collection', null=True, blank=True),
        ),
    ]
