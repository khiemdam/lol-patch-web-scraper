"""
Logic behind sending and formatting emails.
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CSS = """
<head>
    <style>
        * {
            font-family: 'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;
            background-color: #f4f4f4;
            color: #333333;
        }
        h1 {
            padding-left: 20px;
            padding-top: 20px;
        }
        .summary {
            font-style: italic;
        }
        .container {
            width: 100%;
            overflow: hidden;
            display: flex;
        }
        .left_block {
            display: inline-block;
            width: 15%;
            height: 100%;
            text-align: center;
            margin: auto
        }
        .left_block img {
            vertical-align: middle;
        }
        .right_block {
            width: 85%;
            display: inline-block;
            margin-left: 5px;
            margin-right: 20px;
        }
        h2 {
            margin-top: 4px;
            margin-bottom: 4px;
        }
        .summary {
            font-weight: bolder;
            margin-bottom: 15px;
        }
    </style>
</head>
"""

def format_email(patch, info):
    """Create email that contains patch information."""
    # first, we will construct the format of our email
    text = "--------------------------------------------------\n"
    text += f"League of Legends Patch {patch} Summary\n"
    html = f"""<html>{CSS}<body><h1>League of Legends Patch {patch} Summary</h1>"""

    for champ in info:
        if champ['name'] is not None:
            text += "--------------------------------------------------\n"
            html += """<hr><div class="container">"""
            text += f"{champ['name']}\n\n"
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
    return text, html

def send_email(patch, info, sender_email, sender_password):
    """Send patch note info as an email"""
    print("running send_email")

    text, html = format_email(patch, info)
    file_path = "emails.txt"

    with open(file_path, 'r', encoding="utf-8") as file:
        for receiver_email in file:
            message = MIMEMultipart("alternative")
            message["Subject"] = f"League of Legends Patch {patch} Summary"
            message["From"] = sender_email
            message["To"] = receiver_email
            message.attach(MIMEText(text, "plain"))
            message.attach(MIMEText(html, "html"))

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, sender_password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )
