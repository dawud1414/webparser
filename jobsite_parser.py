import urllib
import requests
from bs4 import BeautifulSoup
from email.mime.text import  MIMEText
import pandas as pd
import smtplib
import csv


def load_indeed_jobs_div(job_title, location):
    getVars = {'j' : job_title, 'l' : location, 'fromage' : 'last', 'sort' : 'date'}
    url = ('https://www.indeed.com/m/jobs?' + urllib.parse.urlencode(getVars))
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    job_soup = soup.find(id="resultsBody")
    return job_soup
 
 #Get job Title
def job_title(job_elem):
    title_elem = job_elem.find('h2', class_='title')
    title = title_elem.text.strip()
    return title
  
 #Get company name
def company_name(job_elem):
    company_elem = job_elem.find('span', class_='company')
    company = company_elem.text.strip()
    return company

#Extract links
def extract_link(job_elem):
    link = job_elem.find('a')['href']
    link = 'www.indeed.com/m/' + link
    return link

#Extract dates
def extract_date(job_elem):
    date_elem = job_elem.find('span', class_='date')
    date = date_elem.text.strip()
    return date
        
