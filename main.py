import json
import os

data = {}

def url_encode_string(input_string):
    encoded_string = ''
    for char in input_string:
        if char.isalnum() or char in ['-', '_', '.', '~']:
            encoded_string += char
        else:
            encoded_string += '%' + str(ord(char))
    return encoded_string

for x in os.walk('.'):
    if x[0] != '.' and ".git" not in x[0]:
        folder = url_encode_string(x[0][2:])
        print(f'added {folder}')
        data[folder] = {
                "file":f'https://fluxusthemes.github.io/ThemeFiles/{folder}/theme.flux',
                "preview":f'https://fluxusthemes.github.io/ThemeFiles/{folder}/preview.png'
            }

sorted_dict = {key: data[key] for key in sorted(data)} #Sort
with open('file.json', 'w') as f:
    json.dump(sorted_dict, f, indent=4)
