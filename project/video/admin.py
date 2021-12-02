from django.contrib import admin

from . import models


@admin.register(models.Video)
class Video(admin.ModelAdmin):
    list_display = ('title', 'url', 'registered_in')
