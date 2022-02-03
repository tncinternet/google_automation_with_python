#!/usr/bin/env python3

import os
#import sys
import reports
import emails
import datetime


def get_all_fruits_dict(direc):
    fruit_lists = []
    for root, dirs, files in os.walk(direc):
        for text_file in files:
            fruit_details_dict = {}
            count = 0
            full_path = os.path.join(root, text_file)
            print(full_path)
            with open(full_path, 'r') as fruit_details:
                for line in fruit_details.readlines():
                    line = line.strip()
                    if count == 0:
                        fruit_details_dict['name'] = line
                    if count == 1:
                        fruit_details_dict['weight'] = line
                    if count == 2:
                        fruit_details_dict['description'] = line
                    count += 1
            fruit_lists.append(fruit_details_dict)
    return fruit_lists


def build_paragraph(fruits_lists):
    content = ''
    for fruit_dict in fruits_lists:
        content += "name: " + fruit_dict['name'] + '<br />' + "weight: " + fruit_dict['weight'] + '<br /><br />'
    return content

if not os.path.exists("/tmp"):
    os.mkdir("/tmp")

if __name__ == "__main__":
    #directory = sys.argv[1]
    directory = 'supplier-data/descriptions'

    today = datetime.date.today().strftime("%B %d, %Y")
    sender = "automation@example.com"
    recipient = "student-01-2bb814477945@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"
    title = "Processed Update on " + today

    fruits = get_all_fruits_dict(directory)
    paragraph = build_paragraph(fruits)
    reports.generate_report(attachment_path, title, paragraph)
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)
