<!-- Shields from shields.io -->
![Author][author-shield]
[![LinkedIn][linkedin-shield]][linkedin-url] [![Handshake][handshake-shield]][handshake-url] ![Status][status-shield]

# League of Legends Patch Notes Web Scraper

### Web Scraper that emails you relevant League of Legends information from the most recent patch notes. Utilizes Beautiful Soup to parse through the LoL patch notes, and sends an email with smtplib to whoever the user specified (stylized with MIMEText).

![Website Image](/images/lol-web-scraper.png)

## Table of Contents
* [Motivation](#motivation)
* [Technologies](#technologies)
* [Installation](#installation)
* [How To Use](#how-to-use)
* [To-Do List](#to-do-list)
* [Status](#status)
* [Notes](#notes)
* [Credits](#credits)

## Motivation

Although I am not very good at League of Legends, I find it fun to return to the game and rank up on my favorite champions. However, single updates can often change the dynamic of the game, what matchups are favorable, and which characters are now broken (despite Riot's collective 200 years of experience).

I often find it tedious and annoying to constantly analyze the League of Legends website for their long patch notes, even though that information can be so useful. This is why I decided to learn about web scraping, and how to use it to send myself the important stuff (in a digestable way)!

## Technologies
* Python (Beautiful Soup, MIMEText, smtplib)
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
First, you need an email address to send emails from. You may need to use a [Google App Password](https://support.google.com/accounts/answer/185833?hl=en) for the next steps.

Next, make sure you modify emails.txt. In this file, you should put all of the people that you want to send an email to.

Run the following command:
```
python3 main.py --email youremail@gmail.com --password "google app password here"
```

And you're done! The program will send a summary of the patch notes to whoever you wanted to send it to. The email may end up in a spam folder.

If you are interested, fork my repo and automate this program! I would recommend having this web scraper run once every two weeks/one month, as that is typically when a patch comes out.

## To-Do List
- [X] Initial Structure
    - [X] Create repository and local directory for project
    - [X] Start README
    - [X] Create main.py and requirements.txt
    - [X] Install required libraries and document them
- [X] Web Scraper Skeleton
    - [X] Put necessary libraries in main
    - [X] Test if we can extract information from league website
    - [X] Create function to get html from league website
    - [X] Create function to parse through html (for url of newest patch notes)
    - [X] Repeat for specific patch notes page
    - [X] Create function to send email
- [X] Extract HTML
    - [X] Read about requests
    - [X] Obtain information from home page
    - [X] Implement error checking
    - [X] Repeat for patch notes page
- [X] Parse w/ Beautiful Soup
    - [X] Parse through home page for patch notes url
    - [X] Parse through patch notes page for champion info
- [X] Send email
    - [X] Read documentation
    - [X] Create method to pass in txt of emails to send
    - [X] Start an SMTP connection and context
    - [X] Add style to the email using MIMEText
- [X] Finalize everything on GitHub

## Status
Finished the project! If you have any ideas for improvements, please reach out to me!

## Notes
I divided the work into three different files: main.py, scraper.py, handle_email.py. I tried to focus on splitting up tasks into functions, so that I could debug and read my code much more easier.

With Beautiful Soup, I mainly utilized the .find() and .find_next() member functions to search for unique classes corresponding to the information on the patch notes. I also kept a list of dictionaries datastructure (similar to .json format), so I can see how one could implement a web scraper in a web app.

For emailing, I followed a tutorial that shows how to use SMTP, specifically Google's SMTP server. I used Google's app password feature, but it is possible to utilize other SMTP services. I was also able to essentially create an HTML and CSS file to format my emails with MIMEText, making it much more easy to read and look at.

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
[status-shield]: https://img.shields.io/badge/status-completed-555?style=for-the-badge&labelColor=555&color=03c04a
<!-- https://img.shields.io/badge/status-completed-555?style=for-the-badge&labelColor=555&color=03c04a -->