from django.contrib import admin
from journalists.models import Department, Journalist
# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Journalist)
class JournalistAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'birthday',
        'is_married',
        'salary',
    ]
