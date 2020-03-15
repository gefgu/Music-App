from django.urls import path
from . import views

app_name = "music"
urlpatterns = [
    path('', views.MusicFileListView.as_view(), name="index"),
    path('playlists/', views.PlaylistListView.as_view(), name="playlists"),
    path('playlist/<int:pk>', views.PlaylistDetailView.as_view(), name="playlist_detail"),
    path('create/music', views.MusicCreateView.as_view(), name="upload_music"),
    path('create/playlist', views.PlaylistCreateView.as_view(), name="create_playlist"),
    path('musicPlayer', views.musicPlayer, name="music_player")
]
