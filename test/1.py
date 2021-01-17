import requests
import json
import pymysql
from lxml import etree


def page(url):
    headers = {}
    date = bytes()
    response = requests.get(url, headers=headers, allow_redirects=False)
    domain_name = response.url.split(response.request.path_url)[0]
    tree = etree.HTML(response.text)
    tet = tree.xpath('''//div[@class="board-item-content"]''')
    for i in range(len(tet)):
        i_url = domain_name + tree.xpath('''//div[@class="board-item-content"]//p[@class="name"]/a/@href''')[i]
        name = tree.xpath('''//div[@class="board-item-content"]//p[@class="name"]/a/@title''')[i]
        star = tree.xpath('''//div[@class="board-item-content"]//p[@class="star"]/text()''')[i]
        release_time = tree.xpath('''//div[@class="board-item-content"]//p[@class="realeasetime"]/text()''')[i]
        write_to_DB(i_url, name, star, release_time)

        
def write_to_DB(*args):
    for i in args:
        print(i)


def write_to_json(data):
    with open("data.json", 'w+', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False))


def mysql_db():
    db = pymysql.connect(host='localhost', user='root', password='', port='3306')
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print("Database Version:", data)
    cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
    db.close()


if __name__ == '__main__':
    write_to_DB("1", 1, 1, 12, 3, 4, 57)
