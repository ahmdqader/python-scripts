import requests
import re
import urlparse
import sys


crawled_links = []

def filter_links(url): 
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


def crawl(url):
    for link in filter_links(url):
        link = urlparse.urljoin(target, link)
        link = link.strip('/')

        if target in link and link not in crawled_links:
            print("[+] " + link)
            crawled_links.append(link)
            crawl(link)

try:
    if len(sys.argv) == 2:
        target = sys.argv[1]
        crawl(target)
    else: 
        print("Please enter the target website")
        target = raw_input(">> ")
        crawl(target)
except KeyboardInterrupt:
    print("")



