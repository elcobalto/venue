import requests
from requests.auth import HTTPBasicAuth

from apps.artist.constants import SETLIST_FM_API, SETLIST_FM_API_KEY


def get_artist(mbid: str = None, name: str = None, tmid: str = None):
    url = f"{SETLIST_FM_API}/1.0/search/artists"
    headers = {"Accept": "application/json", "x-api-key": SETLIST_FM_API_KEY}
    parameters = {"p": 1, "sort": "sortName"}
    if mbid:
        parameters.update({"artistMbid": mbid})
    if name:
        parameters.update({"artistName": name})
    if tmid:
        parameters.update({"artistTmid": tmid})
    response = requests.get(url, headers=headers, params=parameters)
    return response.json()


def get_artist_by_mdbid(mbid: str):
    url = f"{SETLIST_FM_API}/1.0/artist/{mbid}"
    response = requests.get(url)
    return response.json()


def get_artist_setlists(mbid: str):
    url = f"{SETLIST_FM_API}/1.0/artist/{mbid}/setlists"
    response = requests.get(url)
    return response.json()
