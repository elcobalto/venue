from django.urls import include, path
from rest_framework import routers

from apps.venue.views import venue

router = routers.DefaultRouter()
router.register("v1/", venue.VenueViewset, basename="v1_venue")

urlpatterns = [
    path("", include(router.urls)),
]
