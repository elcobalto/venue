from django.db import models
from datetime import datetime
from apps.show.models import Show, PerformedSong


class Artist(models.Model):
    disambiguation = models.CharField(max_length=256, blank=True, null=True)
    mbid = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=256)
    setlist_fm_url = models.CharField(max_length=256, blank=True, null=True)
    sort_name = models.CharField(max_length=256, blank=True, null=True)
    tmid = models.CharField(max_length=256, unique=True)

    def get_passed_shows(self):
        today = datetime.today()
        return Show.objects.filter(artist_id=self.id, date__lte=today)

    def get_upcoming_shows(self):
        today = datetime.today()
        return Show.objects.filter(artist_id=self.id, date__gte=today)


class Release(models.Model):
    artist = models.ForeignKey(Artist, on_delete=True, related_name="releases")
    name = models.CharField(max_length=256, default='No release')
    release_date = models.DateField()


class Song(models.Model):
    name = models.CharField(max_length=256)
    release = models.ForeignKey(Release, on_delete=True, related_name="songs")

    def get_artist(self):
        return self.release.artist

    def get_performances(self):
        return PerformedSong.objects.filter(original_song=self.id)
