"""
League of Legends Patch Notes Web Scraper
"""

import sys
import click
import requests
from bs4 import BeautifulSoup
from scraper import parse_patch
from handle_email import send_email

HOME_URL = "https://www.leagueoflegends.com/en-us/news/tags/patch-notes/"

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

def parse_home(html):
    """Search html from leagueoflegends.com for the most recent patch."""
    print("running parse_home")
    soup = BeautifulSoup(html, "html.parser")
    # link to patch notes page is within html tag w/ class:
    # style__Wrapper-sc-1h41bzo-0 style__ResponsiveWrapper-sc-1h41bzo-13 eIUhoC cGAodJ isVisible
    patch_class = "style__Wrapper-sc-1h41bzo-0 "
    patch_class += "style__ResponsiveWrapper-sc-1h41bzo-13 eIUhoC cGAodJ isVisible"

    patch_elements = soup.find_all("a", class_=patch_class)
    # each patch element contains an href in the <a> tag
    # we want the most recent patch (first that appears on the page)
    return "https://www.leagueoflegends.com" + patch_elements[0].get('href')

@click.command()
@click.option('-e', '--email', type=str, required=True, help="Enter your email.")
@click.option('-p', '--password', type=str, required=True, help="Enter your email's password.")
def main(email, password):
    """League of Legends Patch Notes Web Scraper. Sends emails
    of the most relevant info from League's patch notes."""
    home_html = get_html(HOME_URL).content
    patch_url = parse_home(home_html)
    patch_html = get_html(patch_url).content
    patch_name, patch_info = parse_patch(patch_html)
    send_email(patch_name, patch_info, email, password)

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()
