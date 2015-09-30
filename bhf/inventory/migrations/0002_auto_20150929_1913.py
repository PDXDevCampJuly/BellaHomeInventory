# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='inventory.Category'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_id',
            field=models.OneToOneField(to='inventory.ProductVariant'),
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='supplier_id',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='supplier_id',
            field=models.ManyToManyField(to='inventory.Supplier'),
        ),
    ]
