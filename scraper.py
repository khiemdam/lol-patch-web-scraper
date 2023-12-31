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
                    "details": []
                }
            ]
        }
        champ_info["img"] = find_img(champ_element)
        champ_info["name"] = find_name(champ_element)
        champ_info["summary"] = find_summary(champ_element)
        champ_info["changes"] = find_changes(champ_element)
        print(champ_info)
        patch_info.append(champ_info)

    return patch_info

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

def find_changes(elt):
    """Find specifics of champion patch."""
    changes = []
    # Start by finding ability changes
    ability_classes = elt.find_all("h4", class_="change-detail-title")
    if ability_classes:
        for ability_class in ability_classes:
            ability_change = {
                "type": "",
                "details": []
            }
            ability_change["type"] = ability_class.text.strip()
            # details TYPICALLY come after the h4 as an unorderd list
            detail_list = ability_class.find_next("ul")
            if detail_list:
                li_elements = detail_list.find_all("li")
                for li in li_elements:
                    detail = li.get_text().strip()
                    ability_change["details"].append(detail)
            changes.append(ability_change)

    # Sometimes, there will be new champions with unique information
    div_class = elt.find("hr", class_="divider")
    if div_class:
        next_elt = div_class.find_next()
        if next_elt.name == 'ul':
            ability_change = {
                "type": "New Champion",
                "details": []
            }
            li_elements = next_elt.find_all("li")
            for li in li_elements:
                detail = li
                ability_change["details"].append(detail)
            changes.append(ability_change)

    return changes
