# Generated by Django 2.1 on 2018-11-17 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20181117_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='book',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Book'),
        ),
    ]
