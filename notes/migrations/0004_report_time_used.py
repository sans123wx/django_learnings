# Generated by Django 2.1.3 on 2018-11-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_report_time_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_time',
            name='used',
            field=models.BooleanField(default=False, verbose_name='是否已使用'),
        ),
    ]
