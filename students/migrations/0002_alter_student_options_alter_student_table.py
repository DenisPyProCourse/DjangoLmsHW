# Generated by Django 4.0.4 on 2022-05-21 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
    ]
