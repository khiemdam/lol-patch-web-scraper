"""
League of Legends Patch Notes Web Scraper
"""

import sys
import requests

URL = "https://www.leagueoflegends.com/en-us/news/tags/patch-notes/"

def get_home_html():
    """Get the html from leagueoflegends.com and store it."""
    print("running get_html")
    try:
        page = requests.get(URL, timeout=10)
        if page.status_code == 200:
            return page

        print(f"Error: {page.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    sys.exit(1)

get_home_html()
