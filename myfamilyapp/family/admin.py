# family/admin.py

from django.contrib import admin
from .models import Child, CodingSession, PlaytimeSession

class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

class CodingSessionAdmin(admin.ModelAdmin):
    list_display = ('child', 'duration_minutes', 'date')

class PlaytimeSessionAdmin(admin.ModelAdmin):
    list_display = ('child', 'duration_minutes', 'date')

admin.site.register(Child, ChildAdmin)
admin.site.register(CodingSession, CodingSessionAdmin)
admin.site.register(PlaytimeSession, PlaytimeSessionAdmin)
