# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('westgate_estates', '0007_auto_20160511_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save_search',
            name='r_furnished',
            field=models.IntegerField(choices=[(0, b'Furnished'), (1, b'Part Furnished'), (2, b'Unfurnished'), (3, b'Not Specified'), (4, b'Furnished/ Un Furnishedf')], default=-1),
        ),
    ]
