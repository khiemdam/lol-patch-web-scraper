"""
League of Legends Patch Notes Web Scraper
"""

import sys
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import click
import requests
from bs4 import BeautifulSoup
from scraper import parse_patch

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

def send_email(patch, info, sender_email, sender_password):
    """Send patch note info as an email"""
    print("running send_email")

    css = """
    <head>
        <style>
            * {
                font-family: "Comic Sans MS", "Comic Sans", cursive;
                background-color: #f4f4f4;
                color: #333333;
            }
            .summary {
                font-style: italic;
            }
            .container {
                display: flex;
            }
            .left_block {
                display: inline-block;
                margin: auto;
            }
            .right_block {
                display: inline-block;
                margin: auto;
                width: 75%;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
        </style>
    </head>
    """

    # first, we will construct the format of our email
    text = "--------------------------------------------------\n"
    text += f"League of Legends Patch {patch} Summary\n"
    html = f"""<html>{css}<body><h1>League of Legends Patch {patch} Summary</h1>"""

    for champ in info:
        if champ['name'] is not None:
            text += "--------------------------------------------------\n"
            html += "<hr>"
            text += f"""<div class="container">{champ['name']}\n\n"""
            html += f"""
            <div class="left_block">
                <img src="{champ['img']}"alt="Image of {champ['name']}" class="champ_pic">
            </div>
            <div class="right_block">
            """
            html += f"<h2>{champ['name']}</h2>"

            # champions that just got released will not have a summary
            if champ['summary'] is not None:
                text += f"     \"{champ['summary']}\"\n\n"
                html += f"""<div class=summary>"{champ['summary']}"</div>"""


            for change in champ['changes']:
                text += f"{change['type']}:\n"
                html += f"<div class=change_type>{change['type']}</div>"
                html += "<div class=changes><ul>"
                for i, detail in enumerate(change['details']):
                    if change['type'] != "New Champion":
                        text += f"  * {detail}\n"
                        html += f"<li>{detail}</li>"
                    else:
                        text += f"  * {change['new'][i]}\n"
                        html += f"{detail}"
                html += "</ul></div>"
            html += "</div></div>"
    html += "</html></body>"

    file_path = "emails.txt"
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    with open(file_path, 'r', encoding="utf-8") as file:
        for receiver_email in file:
            message = MIMEMultipart("alternative")
            message["Subject"] = f"League of Legends Patch {patch} Summary"
            message["From"] = sender_email
            message["To"] = receiver_email
            message.attach(part1)
            message.attach(part2)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, sender_password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )

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
