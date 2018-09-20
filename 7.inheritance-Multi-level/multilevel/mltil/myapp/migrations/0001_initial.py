# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-20 05:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coustmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
                ('csals', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('coustmer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.Coustmer')),
                ('ename', models.CharField(max_length=20)),
                ('esal', models.IntegerField()),
            ],
            bases=('myapp.coustmer',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('coustmer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.Coustmer')),
                ('sname', models.CharField(max_length=20)),
                ('sfee', models.IntegerField()),
            ],
            bases=('myapp.coustmer',),
        ),
    ]
