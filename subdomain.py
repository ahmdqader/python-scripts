import argparse
import requests


parser = argparse.ArgumentParser(description="Subdomain guesser")
parser.add_argument("host", help="Hostname")
parser.add_argument("-w", "--wordlist", help="Word list.")

args = parser.parse_args()
host = args.host
wordlist = args.wordlist

def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass
    
try:
    wordlist = open(wordlist, 'r')
    for subdomain in wordlist.readlines():
        subdomain = subdomain.strip('\n')
        url = subdomain + '.' + host
        if request(url):
            print('[+] Found new subdomain ' + url)
        
except KeyboardInterrupt:
    print("")