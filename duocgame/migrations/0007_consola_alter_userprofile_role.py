# Generated by Django 5.0.4 on 2024-04-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duocgame', '0006_alter_userprofile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consola',
            fields=[
                ('idConsola', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.TextField()),
                ('releaseDate', models.TextField()),
                ('Storage', models.TextField()),
                ('ram', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('cliente', 'CLIENTE'), ('admin', 'ADMINISTRADOR')], max_length=25),
        ),
    ]