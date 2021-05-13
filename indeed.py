from os import write
import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def load_indeed_jobs(job_title, location):
    getVars = {'q' : job_title, 'l' : location}
    global url
    url = ('https://in.indeed.com/jobs?' + urllib.parse.urlencode(getVars))
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    job_soup = soup.findAll(class_ = "jobsearch-SerpJobCard")
    return job_soup

def getTitle(job_soup):
    for job  in job_soup:
        title = job.find('a', class_='jobtitle')
        yield title.text.strip('\n')

def getCompany(job_soup):
    for job  in job_soup:
        company = job.find('span', class_='company')
        if company:
            yield company.text.strip('\n')

def getSalary(job_soup):
    for job  in job_soup:
        salary = job.find('span', class_='salaryText')
        if salary:
            yield salary.text.strip('\n')
        else:
            yield 'not specified'

def getLocation(job_soup):
    for job  in job_soup:
        location = job.find('div', class_='location')
        if location:
            yield location.text
        else:
            yield 'not specified'

def getSummary(job_soup):
    for job  in job_soup:
        requirements = job.find('div', class_='summary')
        if requirements:
            yield requirements.getText().strip('\n')

def getFullSummary(job_soup):
    options = Options()
    options.add_argument('--headless')  
    options.add_argument('--profile-directory=Default') 
    browser = webdriver.Chrome(options=options)
    for i in range(0,15):
        data_jk  = (str(job_soup[i]["data-jk"]))
        browser.get(url + f"&vjk={data_jk}")
        soup = BeautifulSoup(browser.page_source, "html.parser")
        desc = soup.find('div',class_='jobsearch-jobDescriptionText')
        yield(desc.text)

def getFullUrl(job_soup):
    for i in range(0,15):
        data_jk  = (str(job_soup[i]["data-jk"]))
        yield(url + f"&vjk={data_jk}")

"""
this is the final thing ->

soupObj = load_indeed_jobs('Python Developer', 'India')
full_summary = (str(list(getFullSummary(soupObj))))
summary = list(getSummary(soupObj))
salary = list(getSalary(soupObj))
company = list(getCompany(soupObj))
loc = list(getLocation(soupObj))
titles = list(getTitle(soupObj))
full_url = list(getFullUrl(soupObj))
"""