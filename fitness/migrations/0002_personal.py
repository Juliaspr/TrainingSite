# Generated by Django 4.1.1 on 2022-12-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(help_text='имя', max_length=100, verbose_name='name')),
                ('FIO', models.CharField(help_text='ФИО', max_length=100, verbose_name='FIO')),
                ('Trainer', models.CharField(help_text='тренер', max_length=100, verbose_name='Trainer')),
                ('Goals', models.CharField(help_text='цель', max_length=200, verbose_name='Goal')),
            ],
            options={
                'verbose_name': 'Personal',
                'db_table': 'Personal',
            },
        ),
    ]
