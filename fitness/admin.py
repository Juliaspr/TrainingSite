from django.contrib import admin

from fitness import models

# Register your models here.
admin.site.register(models.Trainers)
admin.site.register(models.Profiles)
admin.site.register(models.GroupPrograms)
