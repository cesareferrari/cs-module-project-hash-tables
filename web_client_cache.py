# build a client that will cache a URL

import urllib.request
import datetime

cache = {}
url = "https://www.google.com"
# given a URL, check if it's in the cache

class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.time_fetched = datetime.datetime.now().timestamp()


def fetch_web_page(url):

    stale_data = True

    if url in cache:
        time_now = datetime.datetime.now().timestamp()
        print("getting from cache")
        cache_entry = cache[url]

        if time_now - cache_entry.time_fetched < 10:
            page = cache_entry.data
            stale_data = False

    # otherwise send out a request to get the web page
    elif stale_data:
        print("getting from internet")
        response = urllib.request.urlopen(url)
        data = response.read()
        response.close()

    # and put the result in our cache
        cache_entry = CacheEntry(data)
        cache[url] = cache_entry
        page = cache[url].data

    return page

page = fetch_web_page(url)
print(page)

also_page = fetch_web_page(url)
