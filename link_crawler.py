import re
from urllib import robotparser
from urllib.parse import urljoin

from DiskCache import DiskCache
from Downloader import Downloader


def link_crawler(seed_url, link_regex, user_agent='wswp', max_depth=4,
                 delay=1, proxies=None, num_retries=2, cache=None):
    if cache is None:
        cache = {}
    crawl_queue = [seed_url]
    seen = {seed_url: 0}
    rp = get_robots(seed_url)
    down = Downloader(delay=delay, user_agent=user_agent, proxies=proxies, cache=cache)
    while crawl_queue:
        url = crawl_queue.pop()
        if rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                print("Skipping %s due to depth" % url)
                continue
            html = down(url, num_retries=num_retries)
            if not html:
                print("Html is None:", url)
                continue
            for link in get_links(html['html']):
                if re.match(link_regex, link):
                    abs_link = urljoin(seed_url, link)
                    if abs_link not in seen:
                        seen[abs_link] = depth + 1
                        crawl_queue.append(abs_link)
        else:
            print('Block by robots.txt:', url)


def get_links(html):
    web_page_regex = re.compile("""<a href=["'](.*?)["']""", re.IGNORECASE)
    return web_page_regex.findall(html)


def get_robots(robots_url):
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp


if __name__ == "__main__":
    link_crawler('http://example.python-scraping.com/',
                 '/places/default/(index|view)/(.*)',
                 cache=DiskCache())
