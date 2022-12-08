# Web parser to scrape data from indeed
import yagmail
import pytest
import requests
from bs4 import BeautifulSoup
import mimetypes
from datetime import datetime
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

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

def email():
    """This function uses yagmail to send email"""
    server = smtplib.SMTP("smtp.gmail.com:587")

    yag = yagmail.SMTP('finalwebscrape@gmail.com', 'Passwordis326')
    yag.send(to = 'finalwebscrape@gmail.com', subject= 'indeed jobs in csv', contents= 'the body', attachments= 'new.csv' )

def main(position, location):
    """Main function run the program and save the data in a csv file"""
    """Send csv file to the user through email"""
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
    

    if email:
        email()
if __name__ == '__main__':       
    main('data scientist', 'maryland')

