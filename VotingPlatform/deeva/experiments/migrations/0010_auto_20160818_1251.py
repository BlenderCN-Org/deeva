# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-18 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0009_auto_20160818_1233'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='individualvariablevalue',
            unique_together=set([('individual', 'variable')]),
        ),
    ]
