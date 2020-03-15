from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import MusicFile, Playlist
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

# Create your views here.
class MusicFileListView(ListView):
    model = MusicFile
    context_object_name = 'musics'
    template_name = 'music/index.html'
    queryset = MusicFile.objects.all().order_by("-id")

class PlaylistListView(ListView):
    model = Playlist
    context_object_name = "playlists"
    template_name = 'music/playlists.html'

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'music/index.html'
    context_object_name = "playlist"

class MusicCreateView(CreateView):
    model = MusicFile
    fields = ['name', 'artist', 'file']
    success_url = reverse_lazy('music:index')
    template_name = 'music/create_form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Upload Music"
        return context

class PlaylistCreateView(CreateView):
    model = Playlist
    fields = ['name', 'musics']
    success_url = reverse_lazy('music:index')

    template_name = 'music/create_form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Create Playlist"
        return context


def musicPlayer(request):
    return render(request, "music/musicPlayer.html")
