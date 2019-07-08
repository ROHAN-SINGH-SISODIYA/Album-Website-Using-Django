from django.db import models
from django.urls import reverse


class Album(models.Model):
    title = models.CharField(max_length=512)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=128)
    logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "Album(" \
               "title='" + self.title + "', " +\
               "artist='" + self.artist + "', " +\
               "genre='" + self.genre + "', " +\
               "logo='" + self.logo + "'" +\
               ")"


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    type = models.CharField(max_length=16)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return "Song("\
               "title='" + self.title + "', " +\
               "type='" + self.type + "', " +\
               "is_favorite=" + str(self.is_favorite) + ", " +\
               "album='" + self.album.title + "'" +\
               ")"
