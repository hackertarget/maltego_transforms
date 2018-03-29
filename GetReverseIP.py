#!/usr/bin/env python

# Maltego Transform to get hosts from HackerTarget.com (Reverse IP Search)
# with a HackerTarget.com Membership get an API key for additional quota (Free has 200 / day limit)


from MaltegoTransform import *
import sys
import os
import requests

APIKEY = ''

ipaddress = sys.argv[1]
hosts = []
m = MaltegoTransform()


try:
    if len(APIKEY) == 80:
        r = requests.get('https://api.hackertarget.com/reverseiplookup/?q=' + ipaddress + '&apikey=' + APIKEY)
    else:
        r = requests.get('https://api.hackertarget.com/reverseiplookup/?q=' + ipaddress)
    if r.status_code == 200 or 'error check' in r.text:
        m.addUIMessage("Error getting results - check input")    
    elif "Error invalid key" in r.text:
        m.addUIMessage("Error invalid key")
    elif "No DNS A records" in r.text:
        m.addUIMessage("No results found from HackerTarget.com")
    elif "API count exceeded" in r.text:
        m.addUIMessage("API count exceeded")
    else:
        hosts = str(r.text).split('\n')
        hosts = filter(None, hosts)
        for i in hosts:
            m.addEntity('maltego.DNSName', i)
    else:
        m.addUIMessage("No results found from Reverse IP Search") 
except Exception as e:
    m.addUIMessage(str(e))
m.returnOutput()


