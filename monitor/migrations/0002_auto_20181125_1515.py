# Generated by Django 2.1.3 on 2018-11-25 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monitor',
            options={'ordering': ['-date'], 'verbose_name': '断网记录', 'verbose_name_plural': '断网记录'},
        ),
    ]
