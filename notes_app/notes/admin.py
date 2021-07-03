from django.contrib import admin

from .models import Notes

# Registering the Notes model to the admin panel
admin.site.register(Notes)