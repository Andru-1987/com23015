# Generated by Django 4.2.2 on 2023-06-23 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinos_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vinos',
            new_name='Vino',
        ),
    ]