name = 'url_but_not_bitly'


def isMatch(url):
    if url.startswith("http://") or url.startswith("https://") and not "bit.ly" in url:
        return True
    return False


def getUrlTitle(s):
    import urllib
    import BeautifulSoup

    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s))

    return soup.title.string

def safebrowsingcheck(url):
    from gglsbl import SafeBrowsingList

    sbl = SafeBrowsingList('')

    if sbl.lookup_url(url) is None:
        return ':D Not in blacklist'
    else:
        return '@@ In the blacklist'

def parse(clipboard_content):
    content = """
Url :
%s

Url Title :
%s

Google SafeBrowsing Check :
%s
""" % (clipboard_content, getUrlTitle(clipboard_content), safebrowsingcheck(clipboard_content))

    return content
