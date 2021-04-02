from django.contrib import admin
from .models import Appeal

# Register your models here.

@admin.register(Appeal)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['appeal_num', 'appeal_owner_name', 'accepted']




