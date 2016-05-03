name = 'SHA-256'

# def decrypt(clipboard_content):

    # import re
    #
    # data = urllib.urlencode({'hash': clipboard_content})
    # req = urllib2.Request('http://ez.no-ip.info/', data)
    # req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36')
    # result = urllib2.urlopen(req).read()
    #
    # match = re.findall("<h3 class='hash'>(.*)</h3>", result)
    #
    # if match:
        # return match[0]

def vt_report(clipboard_content):
    import simplejson
    import urllib
    import urllib2
    # url = "https://www.virustotal.com/vtapi/v2/comments/put"
    # url = "https://www.virustotal.com/vtapi/v2/file/rescan"
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    parameters = {"resource": clipboard_content,
                  "comment": "How to disinfect you from this file... #disinfect #zbot",
                  "apikey": "a264d77db499762fa7de5cf0372c2129a288ff38e02a81e8a4a736ec3667f214"}
    data = urllib.urlencode(parameters)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    json = response.read()
    # print json.positives
    response_dict = simplejson.loads(json)
    return response_dict.get("positives", {})
