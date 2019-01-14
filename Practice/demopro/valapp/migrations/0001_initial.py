# Generated by Django 2.1 on 2019-01-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=8)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
    ]
