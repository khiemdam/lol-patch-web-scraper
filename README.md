<!-- Shields from shields.io -->
![Author][author-shield]
[![LinkedIn][linkedin-shield]][linkedin-url] [![Handshake][handshake-shield]][handshake-url] ![Status][status-shield]

# League of Legends Patch Notes Web Scraper

### Web Scraper that emails you relevant League of Legends information.

## Table of Contents
* [Motivation](#motivation)
* [Technologies](#technologies)
* [Installation](#installation)
* [How To Use](#how-to-use)
* [To-Do List](#to-do-list)
* [Status](#status)
* [Credits](#credits)

## Motivation

Although I am not very good at League of Legends, I find it fun to return to the game and rank up on my favorite champions. However, single updates can often change the dynamic of the game, what matchups are favorable, and which characters are now broken (despite Riot's collective 200 years of experience).

I often find it tedious and annoying to constantly check the League of Legends website for their patch notes, even though that information can be so useful. This is why I decided to learn what webscraping is, and how to use it to send myself the important stuff (in a digestable way)!

## Technologies
* Python (Beautiful Soup)
* Any IDE (I used VSCode)

## Installation
Navigate to your desired directory. In your shell/terminal, type in the following:

With SSH Keys:
```
git clone git@github.com:khiemdam/recipes-website.git
```
With HTTPS:
```
git clone https://github.com/khiemdam/recipes-website.git
```

Make sure you have python installed:

MacOS:
```
brew install python3
```
WSL or Linux:
```
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv python3-wheel python3-setuptools
```

Create a virtual environment and activate it:
```
python3 -m venv env
source env/bin/activate
```

Install all required libraries:
```
pip install -r requirements.txt
```

## How To Use
Run the following command:
```
python3 main.py
```

## To-Do List
- [ ] Initial Structure
    - [X] Create repository and local directory for project
    - [X] Start README
    - [X] Create main.py and requirements.txt
    - [ ] Install required libraries and document them
- [ ] Web Scraper Skeleton
    - [ ] Put necessary libraries in main
    - [X] Test if we can extract information from league website
    - [X] Create function to get html from league website
    - [X] Create function to parse through html (for url of newest patch notes)
    - [X] Repeat for specific patch notes page
    - [ ] Create function to send email
- [X] Extract HTML
    - [X] Read about requests
    - [X] Obtain information from home page
    - [X] Implement error checking
    - [X] Repeat for patch notes page
- [X] Parse w/ Beautiful Soup
    - [X] Parse through home page for patch notes url
    - [X] Parse through patch notes page for champion info
- [ ] Send email
    - [X] Read documentation
    - [ ] Create method to pass in txt of emails to send
    - [ ] Start an SMTP connection and context
    - [ ] Add style to the email using MIMEText
- [ ] Finalize everything on GitHub

## Status
Working on email portion of the program...

## Credits
* [Python Web Scraping Basics](https://realpython.com/python-web-scraping-practical-introduction/#get-to-know-regular-expressions)
* [Python Beautiful Soup Basics](https://realpython.com/beautiful-soup-web-scraper-python/)
* [Python Send Email Basics](https://realpython.com/python-send-email/)
* [Shields and Badges from shields.io](shields.io)
* [Social Icons](https://fontawesome.com/)

<!-- Links & Images -->
[author-shield]: https://img.shields.io/badge/Author-Khiem_Dam-555?style=for-the-badge&color=999
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-555?style=for-the-badge&logo=linkedIn
[linkedin-url]: https://www.linkedin.com/in/khiemd/
[handshake-shield]: https://img.shields.io/badge/Handshake-555?style=for-the-badge&logo=handshake&logoColor=white
[handshake-url]: https://app.joinhandshake.com/stu/users/31441591
[status-shield]: https://img.shields.io/badge/status-WIP-555?style=for-the-badge&color=FFA500
<!-- https://img.shields.io/badge/status-completed-555?style=for-the-badge&labelColor=555&color=03c04a -->