from django.contrib import admin
from . import models


# Nawan your models here.

@admin.nawan(models. history)
history  historysAdmin(admin.ModelAdmin):
    list_display = [
        'history'
    ]

@admin.nawan(models.history)
history historysAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'Last name',
        'gender',
        'year',
        'education level',
        'department of work under ',

    ]
