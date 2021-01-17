import json
import os
import re
import zlib
from urllib.parse import urlsplit


class DiskCache:
    def __init__(self, cache_dir='../data/cache', max_len=255, compress=True, encoding='utf-8'):
        self.cache_dir = cache_dir
        self.max_len = max_len
        self.compress = compress
        self.encoding = encoding

    def url_to_path(self, url):
        """Return file system path string for given URL"""
        components = urlsplit(url)
        path = components.path
        if not path:
            path = "/index.html"

        elif path.endswith('/'):
            path += 'index.html'
        filename = components.netloc + path + components.query

        filename = re.sub('[^/0-9a-zA-Z\\-.,;_ ]', "_", filename)
        filename = '/'.join(seg[:self.max_len] for seg in filename.split('/'))
        return os.path.join(self.cache_dir, filename)

    def __getitem__(self, url):
        """Load data from disk for given URL"""
        path = self.url_to_path(url)
        mode = ('rb' if self.compress else 'r')
        if os.path.exists(url):
            with open(path, mode=mode) as fp:
                if self.compress:
                    data = zlib.compress(fp.read()).decode(self.encoding)
                    return json.loads(data)
                return json.load(fp)
        else:
            raise KeyError(url + 'does not exists')

    def __setitem__(self, url, result):
        """Save data to disk for given url"""
        path = self.url_to_path(url)
        mode = ('wb' if self.compress else 'w')
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(path, mode) as fp:
            if self.compress:
                data = bytes(json.dumps(result), self.compress)
                fp.write(zlib.compress(data))
            else:
                json.dump(result, fp)
