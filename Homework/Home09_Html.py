__author__ = 'stanislav-kuhtinski'

import urllib.request
# import requests

def get_webpage(url):
    responce = urllib.request.urlopen(url)
    print('Responce code is ', responce.code)
    print('Responce Content-Type is ', responce.info()['Content-Type'])
    page_html = responce.read()
    responce.close()
    # print(page_html)

get_webpage('http://habr.com')
