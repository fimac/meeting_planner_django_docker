from django.contrib import admin

# Register your models here.
from .models import Room, Meeting

admin.site.register(Room)
admin.site.register(Meeting)