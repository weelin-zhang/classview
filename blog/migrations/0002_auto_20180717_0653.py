# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-17 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('favor_post', 'give favor post'),)},
        ),
    ]