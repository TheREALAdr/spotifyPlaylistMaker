from bs4 import BeautifulSoup
import requests
import spotipy

movie_date = input("What time do you want to travel to? Type the date in YYYY-MM-DD format here:\n")

WEBSITE_ACCESS_LINK = "https://www.billboard.com/charts/hot-100/"

# tag = <h3 id="title-of-a-story" class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet">
song_title_list = []

response = requests.get(f"{WEBSITE_ACCESS_LINK}{movie_date}")
bs4_data = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
song_data = bs4_data.select("li ul li h3")


for song_item in song_data:
    song_title = song_item.getText().strip()
    song_title_list.append(song_title)

print(song_title_list)