from django.contrib import admin

from backend.vehicle import models


admin.site.register(models.Vehicle)
admin.site.register(models.Parameter)
admin.site.register(models.Data)
