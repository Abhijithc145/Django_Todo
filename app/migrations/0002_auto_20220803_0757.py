# Generated by Django 2.2.12 on 2022-08-03 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='link',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='url',
            name='uuid',
        ),
    ]
