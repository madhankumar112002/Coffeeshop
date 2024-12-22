from django.contrib import admin
from .models import cofee


class cofeeAdmin(admin.ModelAdmin):
    list_display =('name','price','quantity')

admin.site.register(cofee,cofeeAdmin)

