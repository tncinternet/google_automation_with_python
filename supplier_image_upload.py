 #! /usr/bin/env python3

import requests
import sys
import os

directory = sys.argv[1]
url = 'http://localhost/upload/'


for root, dirs, files in os.walk(directory):
    for name in files:
        if name.endswith('.jpeg'):
            full_path = os.path.join(root, name)
            print(full_path)
            with open(full_path, 'rb') as fruit_image:
                r = requests.post(url, files={'file': fruit_image})
            print(r.status_code)