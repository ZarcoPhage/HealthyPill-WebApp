from django.contrib import admin

from HealthyPillApp import models
# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.Event)
admin.site.register(models.Notification)