# Generated by Django 2.1.2 on 2018-11-05 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0023_unit_types_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit_types',
            name='customer',
        ),
    ]
