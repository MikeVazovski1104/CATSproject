from django.contrib import admin

from .models import Guest, Cat, Achievements

# Register your models here.
admin.site.register(Guest)
admin.site.register(Cat)
admin.site.register(Achievements)

