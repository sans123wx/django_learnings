# Generated by Django 2.1.2 on 2018-10-24 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='data',
            new_name='date',
        ),
    ]