""" 28 October 2013.
The page source contains text with mostly symbols. Need to find the characters.
Use urllib.request to import the source code
Use 're' Regular Expression Module to help find the characters.
First, import the source 
Second, find the 'mess'
Third, find the chars
"""

import urllib.request
import re
def get_challenge(s):
    return urllib.request.urlopen('http://www.pythonchallenge.com/pc/' + s).read()
src = str(get_challenge('def/ocr.html'))

start = src.find("<!--\\n%%")

#print(start)
print("****************************************************************")
newsrc = src[start:]
result = str(re.findall("[A-Za-z0-9]", newsrc))
counts = {}
for c in result:
	counts[c] = counts.get(c,0) + 1
print(counts)
answer = ''.join(re.findall("[A-Za-mo-z0-9]", result)) # had to miss out 'n' because couldn't get rid of newlinge chars
print(answer)
