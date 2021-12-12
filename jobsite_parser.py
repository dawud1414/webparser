import requests
from bs4 import BeautifulSoup
from email.mime.text import  MIMEText
from datetime import datetime
import pandas as pd
import smtplib
import csv


def get_url(position, location):
    """Generate url from position and location"""
    temp = 'https://www.indeed.com/jobs?q={}&l={}'
    url = temp.format(position, location)
    return url


def extract(job):
    """This function extract title, company name, summary, post_date, location and salary"""
    
    title = job.find('h2', class_='jobTitle').text.strip()
    company = job.find('span', class_='companyName').text.strip()
    summary = job.find('div', 'job-snippet').text.strip()
    
    post_date = job.find('span','date').text
    date = datetime.today().strftime('%Y-%m-%d')
    location = job.find('div', class_='companyLocation').text.strip()
    salary_tag = job.find('div', 'attribute_snippet')
    
    if salary_tag:
        salary = salary_tag.text.strip()
    else:
        salary = '' 
      
    record = (title, company,post_date, date, salary, location, summary)
    return record


def main(position, location):
    """Main function run the program and save the data in a csv file"""
    records = []
    url = get_url(position, location)
    
    
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('div', 'job_seen_beacon')
        for job in jobs:
            record = extract(job)
            records.append(record)
        
        try:
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
        except AttributeError:
            break
        
  
    with open('new.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['JobTitle', 'Company', 'Date_Listed', 'Extracted Date', 'Salary/Shift', 'Location', 'Summary'])
        writer.writerows(records)
        
main('data scientist', 'maryland')

