# Generated by Django 4.1.2 on 2022-11-01 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employe',
            new_name='Employee',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='ocupattion',
            new_name='occupation',
        ),
    ]
