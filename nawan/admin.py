from django.contrib import admin

# Register your models here.
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = list_display


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "l_name", "gender", "age", "qualification", "department")
    search_fields = list_display