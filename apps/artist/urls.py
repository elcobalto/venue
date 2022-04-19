from django.urls import include, path
from rest_framework import routers

from apps.artist.views import artist, release, song

router = routers.DefaultRouter()
router.register("v1/artist", artist.ArtistViewset, basename="v1_artist")
router.register("v1/release", release.ReleaseViewset, basename="v1_release")
router.register("v1/song", song.SongViewset, basename="v1_song")

urlpatterns = [
    path("", include(router.urls)),
]
