# Generated by Django 2.1.2 on 2018-11-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0028_auto_20181111_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='修复时间',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='到校时间',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='响应时间',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='返校时间',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='通知时间',
            field=models.DateField(blank=True, null=True),
        ),
    ]