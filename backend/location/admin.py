from django.contrib import admin
from .models import TaskerLocation, MapLocation, CustomerLocation, TaskLocation

admin.site.register(CustomerLocation)
admin.site.register(TaskerLocation)
admin.site.register(MapLocation)
admin.site.register(TaskLocation)

# Register your models here.
