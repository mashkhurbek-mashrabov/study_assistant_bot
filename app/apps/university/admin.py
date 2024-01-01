from django.contrib import admin

from university.models import Group, Student


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'telegram_id',)
    search_fields = ('name', 'telegram_id',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'phone', 'telegram_id',)
    list_filter = ('group', 'created_at',)
    search_fields = ('name', 'telegram_id',)
