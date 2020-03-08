from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import MusicFile, Playlist

# Create your views here.
class MusicFileListView(ListView):
    model = MusicFile
    context_object_name = 'musics'
    template_name = 'music/index.html'

class PlaylistListView(ListView):
    model = Playlist
    context_object_name = "playlists"
    template_name = 'music/playlists.html'

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'music/index.html'
    context_object_name = "playlist"
