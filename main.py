import json
import os
import urllib.parse

data = {}

print(url_encoded_string)
for x in os.walk('.'):
    if x[0] != '.' and ".git" not in x[0]:
        title = x[0][2:]
        folder = urllib.parse.quote(title)
        print(f'added {title}')
        data[title] = {
                "file":f'https://fluxusthemes.github.io/ThemeFiles/{folder}/theme.flux',
                "preview":f'https://fluxusthemes.github.io/ThemeFiles/{folder}/preview.png'
            }

sorted_dict = {key: data[key] for key in sorted(data)} #Sort
with open('file.json', 'w') as f:
    json.dump(sorted_dict, f, indent=4)
