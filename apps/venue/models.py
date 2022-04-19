from django.db import models
from datetime import datetime
from apps.show.models import Show


class Venue(models.Model):
    address = models.CharField(max_length=256)
    capacity = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    name = models.CharField(max_length=256)

    def get_passed_shows(self):
        today = datetime.today()
        return Show.objects.filter(venue_id=self.id, date__lte=today)

    def get_upcoming_shows(self):
        today = datetime.today()
        return Show.objects.filter(venue_id=self.id, date__gte=today)
