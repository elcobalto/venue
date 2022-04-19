from rest_framework import serializers

from apps.show.models import PerformedSong


class PerformedSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformedSong
        fields = "__all__"
