from django.contrib import admin

from .models import Guest, Pets, Achievements

# Register your models here.
admin.site.register(Guest)
admin.site.register(Pets)
admin.site.register(Achievements)

