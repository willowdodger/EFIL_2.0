from html.parser import HTMLParser  # to parse html
from urllib import parse


class linkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url  # taking base url
        self.page_url = page_url  # taking page url
        self.links = set()  # passing here set of links

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == "a":  # extracting only starting tags
            for (attribute, value) in attrs:  # getting attribute
                if attribute == "href":
                    url = parse.urljoin(self.base_url, value)  # finding complete url
                    self.links.add(url)  # prideda prie saraso

    def page_links(self):  # page link function
        return self.links
