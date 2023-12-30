"""
League of Legends Patch Notes Web Scraper
"""

import sys
import requests
from bs4 import BeautifulSoup
from scraper import parse_patch

HOME_URL = "https://www.leagueoflegends.com/en-us/news/tags/patch-notes/"
sender_email = "youremail@gmail.com"
password = "yourpasswordhere"

def get_html(url):
    """Get the html from leagueoflegends.com and store it."""
    print(f"running get_html on {url}")
    try:
        page = requests.get(url, timeout=10)
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
    patch_class = "style__Wrapper-sc-1h41bzo-0 "
    patch_class += "style__ResponsiveWrapper-sc-1h41bzo-13 eIUhoC cGAodJ isVisible"

    patch_elements = soup.find_all("a", class_=patch_class)
    # each patch element contains an href in the <a> tag
    # we want the most recent patch (first that appears on the page)
    return "https://www.leagueoflegends.com" + patch_elements[0].get('href')

def send_email(info):
    """Send patch note info as an email"""
    print("running send_email")
    file_path = "emails.txt"
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            print(line.strip())

home_soup = BeautifulSoup(get_html(HOME_URL).content, "html.parser")
patch_url = parse_home(home_soup)
patch_soup = BeautifulSoup(get_html(patch_url).content, "html.parser")
patch_info = parse_patch(patch_url)
send_email(patch_info)
