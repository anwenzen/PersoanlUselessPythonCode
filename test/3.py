import requests
import csv
import re
from lxml import etree


def get_one_parse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML,\
         like Gecko) Chrome/84.0.4147.105 Safari/537.36',

    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def main():
    url = 'http://www.baidu.com/'
    html = get_one_parse(url)
    tree = etree.HTML(html)
    for node in tree.xpath('//span[@class ="title-content-title"]/text()'):
        print(node)


if __name__ == '__main__':
    main()