from bs4 import BeautifulSoup
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth



CLIENTID = os.environ.get("CLIENTID")
CLIENTSECRET = os.environ.get("CLIENTSECRET")

WEBSITE_ACCESS_LINK = "https://www.billboard.com/charts/hot-100/"
movie_date = input("What time do you want to travel to? Type the date in YYYY-MM-DD format here: \n")

song_title_list = []
# Pulling from Billboard website! Take data only when necessary!
# response = requests.get(f"{WEBSITE_ACCESS_LINK}{movie_date}")
bs4_data = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
song_data = bs4_data.select("li ul li h3")


for song_item in song_data:
    song_title = song_item.getText().strip()
    song_title_list.append(song_title)

