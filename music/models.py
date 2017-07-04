from django.db import models
from django.core.urlresolvers import reverse
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=200)
    album_logo = models.FileField(max_length=1000)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ': ' + self.artist


@receiver(pre_delete, sender=Album)
def album_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.album_logo.delete(False)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.album_id})
