""" <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. --> 
So, we need to visit each page getting the numbers from the page content.
Use urllib
first page: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345 """
import urllib.request # module that allows access to web pages
import re

url_stem = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
next_nothing = str(12345)
orig_url = url_stem + next_nothing

def get_page(orig_url): # returns content of the page to be used to find next url
    response = urllib.request.urlopen(orig_url)
    page = response.read()
    return page
    

def get_next_url(page, url_stem):
    new_url = url_stem
    match = re.findall("[0-9]",str(page)) # creates list of numbers from page
    if match == []:
        print(new_url)
        return page
    
    print(match)
    
    for c in match:
        new_url += c
    # print(new_url)
    page = get_page(new_url)
    return page

def get_all_urls(page, url_stem, url):
    url = url_stem
    for count in range(1,400):
        page = get_next_url(page, url_stem)
    
page = get_page(orig_url)
print(page)    
get_all_urls(page, url_stem, orig_url)