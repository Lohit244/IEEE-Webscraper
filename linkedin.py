import urllib
import requests
from bs4 import BeautifulSoup

"""
https://www.linkedin.com/jobs/search/?keywords=python%20developer&location=India
"""

def load_linkedin_jobs(job_title, location):
    # This can be thankfully enough just copy pasted with minor changes
    job_title = (urllib.parse.quote(job_title,safe=''))
    location = (urllib.parse.quote(location,safe=''))
    url = (f'https://www.linkedin.com/jobs/search/?keywords={job_title}&location={location}')
    # print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    ResultSet = soup.find('section',class_='results__list')
    return ResultSet

def getData_Id(soupObj):
    # This Function broke ***A LOT*** dunno why but with webdriver this just didnt wanna work even when the F**ing ***(soup obejct)*** was the damn same...
    # This function worked whin i printed soupObj but not when the first line wasn't to print.. 
    # guessing that this is some sorta wird bug that isn't supposed to happen so i guesss i'll move on
    allData = soupObj.findAll('a', class_='result-card__full-card-link')
    for x in allData:
        yield x["href"]


def getTitle(soupObj):
    title_container = soupObj.findAll('h3', class_='result-card__title')
    for title in title_container:
        yield title.text

def getCompany(soupObj):
    company_container = soupObj.findAll('h4', class_='result-card__subtitle')
    for company in company_container:
        yield company.text

def getLocation(soupObj):
    location_container = soupObj.findAll('span', class_='job-result-card__location')
    for location in location_container:
        yield location.text

def getDate(soupObj):
    allTime = soupObj.findAll('time')
    for a in allTime:
        yield a['datetime'].__str__()

""" 
    ##
    Mini Documentaion id you will of this file
    ##
    soupData = load_linkedin_jobs('Python Developer','India')
    ids = list(getData_Id(soupData))
    titles = list(getTitle(soupData))
    companies = (list(getCompany(soupData)))
    location = list(getLocation(soupData))
    dates = list(getDate(soupData))
"""
