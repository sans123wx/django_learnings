# Generated by Django 2.0.3 on 2018-11-21 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_report_time_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='asp',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='sn',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='telephone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
