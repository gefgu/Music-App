from django.db import models

# Create your models here.
class MusicFile(models.Model):
    file = models.FileField(upload_to='musics/')
    name = models.CharField(max_length=120, default="Music Name")

    @property
    def formatted_name(self):
        return str(self.name).replace(r"'", r"\'")

    def __str__(self):
        return str(self.name)
