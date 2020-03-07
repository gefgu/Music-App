from django.shortcuts import render
from django.views.generic import ListView
from .models import MusicFile

# Create your views here.
class MusicFileListView(ListView):
    model = MusicFile
    context_object_name = 'musics'
    template_name = 'music/index.html'
