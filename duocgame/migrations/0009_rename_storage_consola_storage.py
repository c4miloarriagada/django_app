# Generated by Django 5.0.4 on 2024-04-28 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duocgame', '0008_remove_consola_ram_alter_consola_storage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consola',
            old_name='Storage',
            new_name='storage',
        ),
    ]
