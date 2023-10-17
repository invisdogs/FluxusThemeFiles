import json
import os

data = {}

for x in os.walk('.'):
    if x[0] != '.' and ".git" not in x[0]:
        folder = x[0][2:]
        data[folder] = {
                "file":f'https://fluxusthemes.github.io/ThemeFiles/{folder}/theme.flux',
                "preview":f'https://fluxusthemes.github.io/ThemeFiles/{folder}/preview.png'
            }

with open('file.json', 'w') as f:
    json.dump(data, f, indent=4)