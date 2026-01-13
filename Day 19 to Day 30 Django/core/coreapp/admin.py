from django.contrib import admin
from .models import Student
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age')
    search_fields = ('name', 'email')
    list_filter = ('age',)
    ordering = ('name',)

    readonly_fields = ('email',)