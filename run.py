#! /usr/bin/env python3

import os
import requests
import sys


directory = sys.argv[1]
url = 'http://35.193.254.114/fruits/'

for root, dirs, files in os.walk(directory):
    print(files)
    for text_file in files:
        fruit_details_dict = {}
        count = 0
        full_path = os.path.join(root, text_file)
        text_file_name, extension = text_file.split(".")
        with open(full_path, 'r') as fruit_details:
            for line in fruit_details.readlines():
                line = line.strip()
                if count == 0:
                    fruit_details_dict['name'] = line
                if count == 1:
                    weight = int(line.split(' ')[0])
                    fruit_details_dict['weight'] = weight
                if count == 2:
                    fruit_details_dict['description'] = line
                count += 1
        fruit_details_dict['image_name'] = text_file_name + ".jpeg"
        # fruit_details_json = json.dumps(fruit_details_dict)
        # print(fruit_details_json)
        response = requests.post(url, data=fruit_details_dict)
        print(response.status_code)
        print(response.request.body)
