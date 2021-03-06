from django.contrib import admin
from main.models import Main

@admin.register(Main)
class PersonAdmin(admin.ModelAdmin):
    ordering = ['time_cre']
    search_fields = ['name']
    list_display = ('time_cre', 'time_upd')