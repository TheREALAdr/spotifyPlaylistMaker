from bs4 import BeautifulSoup
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

CLIENTID = os.environ.get("CLIENTID")
CLIENTSECRET = os.environ.get("CLIENTSECRET")
REDIRECTURI = os.environ.get("REDIRECTURI")
CLIENTUSERNAME = os.environ.get("CLIENTUSERNAME")

scope = "playlist-modify-private"
WEBSITE_ACCESS_LINK = "https://www.billboard.com/charts/hot-100/"
movie_date = input("What time do you want to travel to? Type the date in YYYY-MM-DD format here: \n")

song_title_list = []
song_uri_list = []
# Pulling from Billboard website! Take data only when necessary!
response = requests.get(f"{WEBSITE_ACCESS_LINK}{movie_date}")
bs4_data = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
song_data = bs4_data.select("li ul li h3")


# song_data = bs4_data.select("li ul li .c-label")
#
#
# pprint(song_data)

def find_track():
    for song_item in song_data:
        song_title = song_item.getText().strip()
        song_title_list.append(song_title)
        spotify_query = f"track:{song_title}"
        spotifyinit = spotipy.Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENTID, client_secret=CLIENTSECRET,
                                      redirect_uri=REDIRECTURI, username=CLIENTUSERNAME))
        spotify_data = spotifyinit.search(q=spotify_query, limit=1, offset=0, type='track', market=None)
        spotify_song_uri = spotify_data["tracks"]["items"][0]["uri"]
        song_uri_list.append(spotify_song_uri)



find_track()
print(song_uri_list)

# current_user_info = spotifyinit.current_user()
# user_id = spotifyinit.current_user()["id"]
