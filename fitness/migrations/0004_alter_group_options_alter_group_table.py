# Generated by Django 4.1.1 on 2022-12-13 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0003_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Group'},
        ),
        migrations.AlterModelTable(
            name='group',
            table='Group',
        ),
    ]
