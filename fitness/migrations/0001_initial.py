# Generated by Django 4.1.1 on 2022-12-12 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(blank=True, help_text='Введите название программы, которые вы ведете', max_length=100, verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Profile',
                'db_table': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(blank=True, help_text='Введите ваше фио', max_length=100, verbose_name='FIO')),
                ('age', models.IntegerField(blank=True, help_text='Введите ваш возраст', verbose_name='Age')),
                ('education', models.CharField(blank=True, help_text='Введите наименования учреждений,которые вы закончили', max_length=100, verbose_name='Education')),
            ],
            options={
                'verbose_name': 'Trainer',
                'db_table': 'Trainers',
            },
        ),
        migrations.CreateModel(
            name='GroupPrograms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(blank=True, help_text='Укажите продолжительность тренировки в минутах', verbose_name='Time')),
                ('description', models.CharField(blank=True, help_text='Расскажите по-подробнее про вашу тренировкуу', max_length=100, verbose_name='Description')),
                ('profile', models.ForeignKey(help_text='Введите название программы, которые вы ведете', null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.profiles', verbose_name='Profile')),
                ('trainer', models.ForeignKey(blank=True, help_text='Выберите тренера', null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.trainers', verbose_name='Trainer')),
            ],
            options={
                'verbose_name': 'Group program',
                'db_table': 'Group programs',
            },
        ),
    ]
