from django.contrib import admin
from .models import MusicFile, Playlist

# Register your models here.
admin.site.register(MusicFile)
admin.site.register(Playlist)
