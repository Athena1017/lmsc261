import re
import requests

headers = {
    "AIC-User-Agent": "museum-crawler (yzheng6@berklee.edu)",
    "User-Agent": "museum-crawler (yzheng6@berklee.edu)",
}


def format_and_print(data, min, max): 
    art_data = data['data']

    for d in art_data:
        title = d['title']
        artist = d['artist_display']
        date = d['date_display']

       
        if date is None:
            continue
        if artist is None:
            artist = "Unknown artist"

       
        year = re.search(r"\d{4}", date)
        if year is None:
            continue

        if min <= int(year.group()) <= max:
            print(f"{title} is by {artist} which was displayed on {date}")


search = input("What would you like to search? ")
min_year = int(input("What's the minimum year you'd like to search? "))
max_year = int(input("What's the maximum year you'd like to search? "))

params = {
    'q': search,
    'fields': "title,artist_display,date_display" 
}

response = requests.get("https://api.artic.edu/api/v1/artworks/search", params=params, headers=headers)
data = response.json()

print()
format_and_print(data, min_year, max_year)
