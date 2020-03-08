from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import MusicFile, Playlist
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
class MusicFileListView(LoginRequiredMixin, ListView):
    model = MusicFile
    context_object_name = 'musics'
    template_name = 'music/index.html'

class PlaylistListView(LoginRequiredMixin, ListView):
    model = Playlist
    context_object_name = "playlists"
    template_name = 'music/playlists.html'

class PlaylistDetailView(LoginRequiredMixin, DetailView):
    model = Playlist
    template_name = 'music/index.html'
    context_object_name = "playlist"

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "music/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, "music/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')
