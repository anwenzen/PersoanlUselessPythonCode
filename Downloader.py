import requests
from random import choice
from Throttle import Throttle


class Downloader:
    def __init__(self, delay=5, user_agent=None, proxies=None, cache=None):
        if cache is None:
            cache = {}
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.cache = cache
        self.num_retries = None

    def __call__(self, url, num_retries=2):
        self.num_retries = num_retries
        try:
            result = self.cache[url]
            print("Loaded from cache:", url)
        except KeyError:
            result = None
        if result and self.num_retries and 500 <= result['code'] < 600:
            result = None
        if result is None:
            self.throttle.wait(url)
            proxies = choice(self.proxies) if self.proxies else None
            headers = {'User-agent': self.user_agent}
            result = self.download(url, headers, proxies, self.num_retries)
            if self.cache:
                self.cache[url] = result
        return result

    def download(self, url, headers, proxies, num_retries):
        print("downloading:", url)
        try:
            resp = requests.get(url, headers=headers, proxies=proxies)
            html = resp.text
            if resp.status_code >= 400:
                print('Download error:', resp.text)
                html = None
                if num_retries and 500 <= resp.status_code < 600:
                    return self.download(url, num_retries - 1)
            return {'html': html, 'code': resp.status_code}

        except requests.exceptions.RequestException as e:
            print("Download error:", e)
            return None
