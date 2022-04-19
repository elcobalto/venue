import requests

from apps.artist.constants import SETLIST_FM_API


def get_artist(mbid: str):
    url = f"{SETLIST_FM_API}/1.0/artist/{mbid}"
    response = requests.get(url)
    return response.json()


def get_artist_setlists(mbid: str):
    url = f"{SETLIST_FM_API}/1.0/artist/{mbid}/setlists"
    response = requests.get(url)
    return response.json()
