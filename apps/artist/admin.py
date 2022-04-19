from django.contrib import admin

from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("mbid", "name", "tmid")


admin.site.register(Artist, ArtistAdmin)
