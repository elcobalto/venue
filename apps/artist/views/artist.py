import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.http import JsonResponse
from apps.artist.models import Artist
from apps.artist.serializers.artist_serializer import ArtistSerializer
from apps.artist.services.setlist_fm import get_artist

logger = logging.getLogger(__name__)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20


class ArtistViewset(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ArtistSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)

    def get_serializer_class(self):
        return ArtistSerializer

    def get_queryset(self):
        return Artist.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@api_view(["GET"])
def get_by_name(request, name):
    artists = Artist.objects.filter(name=name).values()
    if artists:
        return JsonResponse({"artists": list(artists)})
    retrieve_artists = get_artist(name=name)
    artists = retrieve_artists['artist']
    for artist in artists:
        artist_object = Artist(
            disambiguation=artist["disambiguation"] if "disambiguation" in artist else None,
            mbid=artist["mbid"],
            name=artist["name"],
            setlist_fm_url=artist["url"],
            sort_name=artist["sortName"],
            tmid=artist["tmid"] if "tmid" in artist else None,
        )
        artist_object.save()
    return Response(artists['artist'])
