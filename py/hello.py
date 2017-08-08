import urllib2
import re

request = urllib2.Request("http://www.hiyd.com/insanity/1174/")
response = urllib2.urlopen(request)
resp_html = response.read()
print resp_html



