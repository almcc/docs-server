# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_auto_20151002_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ManyToManyField(to='librarian.Collection', blank=True),
        ),
    ]
