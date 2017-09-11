# we will launch multiple spiders
from urllib.request import urlopen
from linkFinder import linkFinder
from functionsForCrawler import *
from domain import *


class spider:  # padarysim kad spideris galetu buti ne vienas o 10 ir daugiau
    project_name = ""
    base_url = ""
    domain_name = ""  # nustatysim cia kad imtu linkus tik is vieno saito, o ne eitu is veno i kita!!!
    queue_file = ""
    crawled_file = ""
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        spider.project_name = project_name
        spider.base_url = base_url
        spider.domain_name = domain_name
        spider.queue_file = spider.project_name + "/queue.txt"
        spider.crawled_file = spider.project_name + "/crawled.txt"
        self.boot()  # will create project name, will contain queue.txt and crawled.txt files
        self.crawl_page("First spider", spider.base_url)  # it will crawl whole page

    @staticmethod
    def boot():
        create_project_dir(spider.project_name)  # create root directory
        create_data_files(spider.project_name, spider.base_url)  # create data files
        spider.queue = file_to_set(spider.queue_file)  # converting queue file and storing to set
        spider.crawled = file_to_set(spider.crawled_file)  # converting crawl file and storing to set

    @staticmethod
    def crawl_page(thread_name, page_url):  # thread name - one instance to crawl page with page url
        if page_url not in spider.crawled:  # checking did we crawled or not
            print(thread_name + "Now crawling " + page_url)  # which page is been crawling
            print("Queue" + str(len(spider.queue)) + " | Crawled " +
                  str(len(spider.crawled)))  # gives the number of files that are crawled
            spider.add_links_to_queue(spider.gather_links(page_url))
            spider.queue.remove(page_url)  # removes crawled url
            spider.crawled.add(page_url)  # adds to crawled file url
            spider.update_files()  # updating files

    @staticmethod
    def gather_links(page_url):
        # decode html to have row code
        html_string = ""
        try:
            response = urlopen(page_url)
            if "text/html" in response.getheader("Content-Type"):  # grazins viska kas yra text/html in content type
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")  # puting bytes to string
            finder = linkFinder(spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in spider.queue) or (url in spider.crawled):
                continue
            if spider.domain_name != get_domain_name(url):  # salyga kad tik konkreciame domaine tikrintu
                continue
            spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(spider.queue, spider.queue_file)
        set_to_file(spider.crawled, spider.crawled_file)
