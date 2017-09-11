import threading
from queue import Queue
from crawler import spider
from domain import *
from functionsForCrawler import *


HOME_PAGE = "http://edrana.lt/"
DOMAIN_NAME = get_domain_name(HOME_PAGE)
PROJECT_NAME = DOMAIN_NAME
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawler.txt"
NUMBER_OF_THREADS = 10  # number of process will work at one time
queue = Queue()
spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)


# how the spider will work
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " Links in the queue")  # how much links left
        create_jobs()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
        crawl()


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)  # creating threading
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

create_workers()
crawl()