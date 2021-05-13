from linkedin import getLocation
import urllib
import requests
from bs4 import BeautifulSoup

"""
https://www.naukri.com/search?k=python%20developer&l=india
"""

def load_naukri_jobs(job_title, location):
    # This can be thankfully enough just copy pasted with minor changes
    job_title = (urllib.parse.quote(job_title,safe=''))
    location = (urllib.parse.quote(location,safe=''))
    url = (f'https://www.naukri.com/search?k={job_title}&l={location}')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    ResultSet = soup.find('div',class_='srp_container')
    return ResultSet

def getTitle(soupObj):
    job = soupObj.findAll('div', class_="row")
    for x in job:
        title = x.find('li', class_='desig')
        if title:
            yield title.text

def getCompany(soupObj):
    job = soupObj.findAll('span', class_="org")
    for org in job:
        yield org.text

def getCompanyRating(soupObj):
    job = soupObj.findAll('a', class_="rating")
    for rating in job:
        if rating:
            yield rating.text
        else:
            yield 'N/A'

def getLocation(soupObj):
    locn_container = soupObj.findAll('span', class_="loc")
    for locn in locn_container:
        yield(locn.text)

def getUrl(soupObj):
    job = soupObj.findAll('div', class_="row")
    for x in job:
        title = x.find('li', class_='desig')
        if title:
            yield (x["data-url"]).__str__()

def getExp(soupObj):
    exp_container = soupObj.findAll('span', class_="exp")
    for exp in exp_container:
        yield(exp.text)

def getSalary(soupObj):
    salary_container = soupObj.findAll('span', class_="salary")
    for salary in salary_container:
        yield(salary.text)

""" 
    a = load_naukri_jobs('python developer','India')
    titles = list(getTitle(a))
    company = list(getCompany(a))
    rating = list(getCompanyRating(a))
    loc = list(getLocation(a))
    url = list(getUrl(a))
    exp = list(getExp(a)) 
    salary= list(getSalary(a)) 
    """