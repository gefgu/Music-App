from django.db import models

# Create your models here.
class MusicFile(models.Model):
    file = models.FileField(upload_to='musics/')
    name = models.CharField(max_length=120, default="Music Name")
    artist = models.CharField(max_length=120)

    @property
    def formatted_name(self):
        return str(self.name).replace(r"'", r"\'")

    def __str__(self):
        return str(self.name) + "\t-\t" + str(self.artist)


class Playlist(models.Model):
    name = models.CharField(max_length=120)
    musics = models.ManyToManyField(MusicFile)

    def __str__(self):
        return self.name
