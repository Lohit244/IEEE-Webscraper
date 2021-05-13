from requests import get
from bs4 import BeautifulSoup
import urllib

def fetch_results(search_term, number_results, language_code):
    #ngl this usr agent string is copied but the code breaks without it so.. to future me ->
    # **DO NOT TOUCH THIS THING IS PERFECT!!**
    usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/61.0.3163.100 Safari/537.36'}
    escaped_search_term = (urllib.parse.quote(search_term,safe=''))
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results+1,language_code)
    response = get(google_url, headers=usr_agent)
    #in case of somthing wrong... im doomed
    response.raise_for_status()
    return response.text

def parse_h3(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'LC20lb DKV0Md'})
        if link and title:
            yield title

def parse_links(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'LC20lb DKV0Md'})
        if link and title:
            if (link['href'])[0] != '/':
                #handle relative urls
                yield str(link['href'])
            else:
                #humane cases..
                yield ("https://www.google.com"+str(link['href']))
def parse_desc(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        link = result.find('a', href=True)
        desc = result.find('span', attrs={'class': 'aCOpRe'})
        if link and desc:
            if (desc.text != ''):
                #good ol' normal everyday sarch stuff
                yield str(desc.text)
            else:
                #description empty... sounds illegal but for some reason google allows that
                yield 'No Description On Google'

def search(term):
    # im getting first 11 results but i don't do anything for 2nd to 11th.. cuz i am too lazy and i read the instructions for the project wrong FML!!
    html = fetch_results(term, 11, 'en')
    titles = []
    ret = []
    links_list = (list(parse_links(html)))
    desc = list(parse_desc(html))
    #probably an easy change to make it slightly faster but 1 and 10 shouldn't be a very big / noticable difference in speed
    titles_html = (list(parse_h3(html))[0:9])
    for title_html in titles_html:
        titles.append(str(title_html)[26:-5])
    for i in range(0,9):
        ret.append([titles[i] , links_list[i], desc[i]])
    return(ret)


"""
Test cases to check -
Elon Musk  --> everything normal and dandy
Python Developer  --> google becomes oversmart and breaks sh*t
Re:Zero --> For the weeb in me!
Programming jobs  --> Nothing special but close to the actual usecases
"""
if __name__ == "__main__":
    search_stack = ["Elon Musk", "Python Developer","Re:Zero","Programming Jobs"]
    for query in search_stack:
        print("\n" + query + "  :")
        print(search(query)[0])