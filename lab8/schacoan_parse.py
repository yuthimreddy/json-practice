#!/usr/bin/env python3

import json

file_path = '/Users/yuthimadireddy/DS2022_YM/my-work/json-practice/lab8/schacon.repos.json'

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    with open('schacon.csv', 'w') as csv_file:
        for repo in data[:5]:
            name = repo.get('name', '')
            html_url = repo.get('html_url', '')
            updated_at = repo.get('updated_at', '')
            visibility = repo.get('visibility', '')
            line = f"{name},{html_url},{updated_at},{visibility}\n"
            csv_file.write(line)

except FileNotFoundError:
    print(f"Error: File not found at path: {file_path}")
except json.JSONDecodeError:
    print(f"Error: File is not valid JSON: {file_path}")

