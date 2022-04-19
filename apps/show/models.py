from django.db import models
from datetime import datetime
from apps.artist.models import Song, Artist
from apps.venue.models import Venue


class Show(models.Model):
    artist = models.ForeignKey(Artist, on_delete=True, related_name="shows")
    date = models.DateField()
    tour = models.CharField(max_length=256)
    venue = models.ForeignKey(Venue, on_delete=True, related_name="shows")

    def get_str_date(self):
        return self.date.strftime('%Y-%m-%d')

    def get_status(self):
        today = datetime.today().strftime('%Y-%m-%d')
        date = self.get_str_date()
        if date < today:
            return 'PERFORMED'
        elif date == today:
            return 'TODAY'
        else:
            return 'UPCOMING'

    def get_artist(self):
        return self.artist


class PerformedSong(models.Model):
    name = models.CharField(max_length=256)
    original_song = models.ForeignKey(Song, on_delete=True, related_name="live_performances")
    show = models.ForeignKey(Show, on_delete=True, related_name="songs")

    def get_performed(self):
        return self.show.get_artist()

    def is_cover(self):
        return self.original_song.get_artist().id != self.show.get_artist().id
