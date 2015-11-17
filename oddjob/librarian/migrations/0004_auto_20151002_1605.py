# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_auto_20151002_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.ManyToManyField(related_name='products', to='librarian.Collection', blank=True),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='release',
            field=models.ForeignKey(related_name='artifacts', to='librarian.Release'),
        ),
        migrations.AlterField(
            model_name='release',
            name='product',
            field=models.ForeignKey(related_name='releases', to='librarian.Product'),
        ),
    ]
