import json
from PIL import Image
import requests
from email.message import EmailMessage
import mimetypes
import os.path
import smtplib
import getpass
import report_email

#report_email.generate_pdf('fruittext')


def optional(arg1, arg2, arg3=None):
    print(arg1)
    print(arg2)
    print(arg3)


optional('a', 'b', 'c')

# changeImage.conv_image('images/Clean-Professional-Creative-and-Modern-Resume-CV-Curriculum-Vitae-Design-Template-Image-Preview.jpg')
# changeImage.conv_all_images('images/')
# fruits = run.dict_fruits('fruittext')
# print(fruits)
# paragraph = ''
# for fruit in fruits:
#     paragraph += "name: " + fruit['name'] + '<br />' + "weight: " + fruit['weight'] + '<br /> <br />'
# print(paragraph)
# reports.generate_report('images/processed.pdf', 'Processed Update on', paragraph)


# from reportlab.lib.units import inch
# from reportlab.platypus import SimpleDocTemplate
# from reportlab.platypus import Paragraph, Spacer, Table, Image
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
# from reportlab.graphics.shapes import Drawing
# from reportlab.graphics.charts.piecharts import Pie
#
# fruit = {
#     "elderberries": 1,
#     "figs": 1,
#     "apples": 2,
#     "durians": 3,
#     "bananas": 5,
#     "cherries": 8,
#     "grapes": 13
# }
#
# report = SimpleDocTemplate('images/doc.pdf')
# styles = getSampleStyleSheet()
# report_title = Paragraph('A Complete Inventory of My Fruit', styles['h1'])
# table_data = []
# for k, v in fruit.items():
#     table_data.append([k, v])
# table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
# report_table = Table(data=table_data, style=table_style, hAlign='LEFT')
#
# report_pie = Pie(width=3*inch, height=3*inch)
# report_pie.data = []
# report_pie.labels = []
#
# for fruit_name in sorted(fruit):
#     report_pie.data.append(fruit[fruit_name])
#     report_pie.labels.append(fruit_name)
# report_chart = Drawing()
# report_chart.add(report_pie)
#
# report.build([report_title, report_table, report_chart])

# message = EmailMessage()
#
# sender = "siviart.sg@gmail.com"
# recipient = "siviart.sg@gmail.com"
# body = """Hey there,
# I am learning to send message using python"""
#
# message['From'] = sender
# message['To'] = recipient
# message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
# message.set_content(body)

# attachment_path = 'images/Clean-Professional-Creative-and-Modern-Resume-CV-Curriculum-Vitae-Design-Template-Image-Preview.jpg'
# attachment_filename = os.path.basename(attachment_path)
#
# print(attachment_filename)
#
# mime_type, _ = mimetypes.guess_type(attachment_path)
# mime_type, mime_subtype = mime_type.split('/')
# print(mime_type, mime_subtype)
#
# with open(attachment_path, 'rb') as ap:
#     message.add_attachment(ap.read(), maintype = mime_type, subtype = mime_subtype, filename = os.path.basename(attachment_path))
# print(message)
#
# mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
# mail_pass = getpass.getpass('Password? ')
# mail_server.login(sender, mail_pass)

# p = {"description": "white kitten",
#      "name": "Snowball",
#      "age_months": 6
#      }
#
# json_p = json.dumps(p)
# print(json_p)
# response = requests.get("https://example.com/path/to/api", data=json_p)
# print(response.request.body)

# people = [
#     {
#         "name": "Sabrina Green",
#         "username": "sgreen",
#         "phone": {
#             "office": "802-223-457",
#             "cell": "802-333-4124"
#         },
#         "department": "IT Infrastructure",
#         "role": "System Administrator"
#     },
#     {
#         "name": "Eli Jones",
#         "username": "ejones",
#         "phone": "565-224-675",
#         "department": "IT Infrastructure",
#         "role": "IT Specialist"
#     },
# ]
#
# my_list = ["John", "Jennie", "Jacob", "Julia"]
#
# my_dict = {
#     "name": "Sabrina Green",
#     "username": "sgreen",
#     "phone": {
#         "office": "802-223-457",
#         "cell": "802-333-4124"
#     },
#     "department": "IT Infrastructure",
#     "role": "System Administrator"
# }


# with open('people.yaml', 'w') as people_yaml:
#     yaml.safe_dump(people, people_yaml)
#     people_yaml.close()

# with open('people.json', 'w') as people_json:
#     json.dump(people, people_json, indent=2)
#     people_json.close()

# with open('people.json', 'r') as json_people:
#     people_dict = json.load(json_people)
#     print(people_dict[1]['name'])
