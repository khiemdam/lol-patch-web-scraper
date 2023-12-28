"""
League of Legends Patch Notes Web Scraper
"""

import sys
import requests
from bs4 import BeautifulSoup

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

def parse_home(soup):
    """Search html from leagueoflegends.com for the most recent patch."""
    print("running parse_home")
    # link to patch notes page is within html tag w/ class:
    # style__Wrapper-sc-1h41bzo-0 style__ResponsiveWrapper-sc-1h41bzo-13 eIUhoC cGAodJ isVisible
    patch_class = "style__Wrapper-sc-1h41bzo-0 style__ResponsiveWrapper-sc-1h41bzo-13 eIUhoC cGAodJ isVisible"
    patch_elements = soup.find_all("a", class_=patch_class)
    # each patch element contains an href in the <a> tag
    # we want the most recent patch (first that appears on the page)
    return "https://www.leagueoflegends.com" + patch_elements[0].get('href')

soup = BeautifulSoup(get_home_html().content, "html.parser")
PATCH_URL = parse_home(soup)
print(PATCH_URL)