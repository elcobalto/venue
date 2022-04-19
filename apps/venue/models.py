from datetime import datetime

from django.db import models


class Venue(models.Model):
    address = models.CharField(max_length=256)
    capacity = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    name = models.CharField(max_length=256)

    def get_passed_shows(self):
        today = datetime.today()
        return self.shows.filter(venue_id=self.id, date__lte=today)

    def get_upcoming_shows(self):
        today = datetime.today()
        return self.shows.filter(venue_id=self.id, date__gte=today)
