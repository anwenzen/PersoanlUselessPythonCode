import csv
import os
import re

from lxml import etree


class CsvCallback:
    def __init__(self):
        self.fields = ('area', 'population', 'ios', 'country_or_district', 'capital',
                       'continent', 'tld', 'currency_code', 'currency_name', 'phone',
                       'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
        # folder = os.path.dirname('../data')
        if not os.path.exists('../data'):
            os.makedirs('../data')
        self.writer = csv.writer(open("../data/data.csv", 'w'))
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        if re.search('/view/', url):
            tree = etree.HTML(html)
            all_rows = []
            for field in self.fields:
                word = tree.xpath('//*[@id="places_%s__row"]/td[2]/text()' % field)
                if word:
                    all_rows.append(word[0])
                else:
                    all_rows.append("")
            self.writer.writerow(all_rows)
