from django.db import models


# Create your models here.
class Trainers(models.Model):
    fio = models.CharField(max_length=100, blank=True, verbose_name="FIO",
                           null=False, help_text="Введите ваше фио")
    experience = models.IntegerField(blank=True, verbose_name="experience", null=True, help_text="Введите опыт работы")
    # work_experience = models.CharField(max_length=100, blank=True, verbose_name="Work_experience",
    #                                    null=False, help_text="Расскажите о вашем опыте работы в сфере фитнеса")
    description = models.CharField(max_length=10000, blank=True, verbose_name="Description",
                                   null=False, help_text="Введите описание тренера")

    class Meta:
        db_table = "Trainers"
        verbose_name = "Trainer"

    def __str__(self):
        return self.fio


class Profiles(models.Model):
    profile = models.CharField(max_length=100, blank=True, verbose_name="Profile",
                               null=False, help_text="Введите название программы, которые вы ведете")

    class Meta:
        db_table = "Profiles"
        verbose_name = "Profile"

    def __str__(self):
        return self.profile


class GroupPrograms(models.Model):
    time = models.IntegerField(blank=True, verbose_name="Time",
                               null=False, help_text="Укажите продолжительность тренировки в минутах")

    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE, verbose_name="Profile",
                                null=True, help_text="Введите название программы, которые вы ведете")

    description = models.CharField(max_length=100, blank=True, verbose_name="Description",
                                   null=False, help_text="Расскажите по-подробнее про вашу тренировкуу")

    trainer = models.ForeignKey(Trainers, on_delete=models.CASCADE, blank=True, verbose_name="Trainer",
                                null=True, help_text="Выберите тренера")

    class Meta:
        db_table = "Group programs"
        verbose_name = "Group program"

    def __str__(self):
        return self.description


class Personal(models.Model):
    Username = models.CharField(max_length=100, blank=False, null=False, verbose_name="name", help_text="имя")
    FIO = models.CharField(max_length=100, blank=False, null=False, verbose_name="FIO", help_text="ФИО")
    Trainer = models.CharField(max_length=100, blank=False, null=False, verbose_name="Trainer", help_text="тренер")
    Goals = models.CharField(max_length=200, blank=False, null=False, verbose_name="Goal", help_text="цель")

    class Meta:
        db_table = "Personal"
        verbose_name = "Personal"


class Group(models.Model):
    Probability = models.CharField(max_length=100, blank=True, null=False, verbose_name="probability",
                                   help_text="С какой вероятностью Вы посетите тренировку?")
    Username = models.CharField(max_length=100, blank=False, null=False, verbose_name="name", help_text="имя")
    Email = models.CharField(max_length=100, blank=False, null=False, verbose_name="email", help_text="почта")

    class Meta:
        db_table = "Group"
        verbose_name = "Group"
