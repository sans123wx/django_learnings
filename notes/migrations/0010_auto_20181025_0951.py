# Generated by Django 2.1.2 on 2018-10-25 01:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_remove_notes_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notes',
            name='类别',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='notes.Unit_types'),
            preserve_default=False,
        ),
    ]
