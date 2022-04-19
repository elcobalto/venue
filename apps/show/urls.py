from django.urls import include, path
from rest_framework import routers

from apps.show.views import performed_song, show

router = routers.DefaultRouter()
router.register("v1/", show.ShowViewset, basename="v1_show")
router.register(
    "v1/perfomed_song",
    performed_song.PerformedSongViewset,
    basename="v1_performed_song",
)

urlpatterns = [
    path("", include(router.urls)),
]
