# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-14 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20180914_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.OneToOneField(null=True, on_delete=models.SET(3), to='myapp.Student'),
        ),
    ]
