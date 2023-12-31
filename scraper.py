"""
Logic behind the League of Legends Patch Notes Web Scraper
"""

from bs4 import BeautifulSoup

def parse_patch(html):
    """Search patch notes for relevant info."""
    print("running parse_patch")
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.get_text())

    patch_info = []

    # Champions
    # class: patch-change-block white-stone accent-before
    champ_elements = soup.find_all("div",
                                   class_="patch-change-block white-stone accent-before")
    for champ_element in champ_elements:
        champ_info = {
            "img": "",
            "name": "",
            "summary": "",
            "changes": [
                {
                    "type": "",
                    "details": ""
                }
            ]
        }
        champ_info["img"] = find_img(champ_element)
        champ_info["name"] = find_name(champ_element)
        champ_info["summary"] = find_summary(champ_element)
        print(champ_info)
        patch_info.append(champ_info)

    return soup

def find_img(elt):
    """Find img src for patched champion."""
    # Find the 'a' tag with class 'reference-link'
    img_class = elt.find("a", class_="reference-link")

    # If 'a' tag is found, find the 'img' tag within it
    if img_class:
        img_tag = img_class.find("img")
        img_tag = img_tag["src"] if img_tag else None
    else:
        img_tag = None

    return img_tag

def find_name(elt):
    """Find name of patched champion."""
    title_class = elt.find("h3", class_="change-title")
    if title_class:
        name = title_class.find("a").text.strip()
    else:
        name = None
    return name

def find_summary(elt):
    """Find summary of champion patch."""
    summary_class = elt.find("p", class_="summary")
    if summary_class:
        summary = summary_class.text.strip()
    else:
        summary = None
    return summary
