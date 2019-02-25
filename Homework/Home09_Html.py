__author__ = 'stanislav-kuhtinski'

import urllib.request
from pathlib import Path
import re
import json


def get_webpage(url):
    try:
        responce = urllib.request.urlopen(url)
    except Exception as error:
        print("Page not found or path is incorrect ", error)
    print('Responce code is ', responce.code)
    print('Responce Content-Type is ', responce.info()['Content-Type'])
    html_bytes = responce.read()
    responce.close()
    return html_bytes


def convert_html(html_bytes):
    html_str = html_bytes.decode("utf8")
    html_split = html_str.split('\n')
    return html_split


def get_links(html_split):
    url_list = []
    regex_url = r'https?:\/\/(?!habr)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),])+'
    for line in html_split:
        # print(line)
        url = re.findall(regex_url, line)
        if url and url is not isinstance(url, type(None)):
            url_list.append(url)
    return url_list


def clean_links(urls_list):
    return None


def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as filehandle:
        filehandle.write(json.dumps(content, indent=4))
    print('Data has been sucessfully save to', filename)


url_list = []
html_bytes = get_webpage('http://habr.com/ru/')
html_split = convert_html(html_bytes)
urls_list = get_links(html_split)
print(*urls_list, sep='\n')
