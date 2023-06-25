from django.contrib import admin

from .models import BiodataModel


@admin.register(BiodataModel)
class BiodataModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'gender', 'nationality',
     'city',  'occupation', 
    )
    ordering = ('name',)
    search_fields = ('name', 'gender', 'city', 'nationality', 'occupation','division',)

