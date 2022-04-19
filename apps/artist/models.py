from datetime import datetime

from django.db import models

from apps.artist.services import setlist_fm


class Artist(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    disambiguation = models.CharField(max_length=256, blank=True, null=True)
    mbid = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=256)
    setlist_fm_url = models.CharField(max_length=256, blank=True, null=True)
    sort_name = models.CharField(max_length=256, blank=True, null=True)
    tmid = models.CharField(max_length=256, blank=True, null=True)

    def get_passed_shows(self):
        today = datetime.today()
        return self.shows.filter(artist_id=self.id, date__lte=today)

    def get_upcoming_shows(self):
        today = datetime.today()
        return self.shows.filter(artist_id=self.id, date__gte=today)

    def get_setlist_fm_artist(self):
        return setlist_fm.get_artist(self.mbid, self.name, self.tmid)

    def get_setlist_fm_artist_by_mbid(self):
        return setlist_fm.get_artist_by_mdbid(self.mbid)

    def get_setlist_fm_artist_setlists(self):
        return setlist_fm.get_artist_setlists(self.mbid)


class Release(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="releases"
    )
    name = models.CharField(max_length=256, default="No release")
    release_date = models.DateField()


class Song(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    name = models.CharField(max_length=256)
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name="songs")

    def get_artist(self):
        return self.release.artist

    def get_performances(self):
        return self.live_performances
