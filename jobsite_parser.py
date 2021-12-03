import requests
from bs4 import BeautifulSoup
from email.mime.text import  MIMEText
import pandas as pd
import smtplib
import csv


for i in range(0,20,10):
    
    url = requests.get(f"https://www.indeed.com/jobs?q=data%20analyst%20&l=Washington%2C%20DC&start=0").text
    soup = BeautifulSoup(url, 'html.parser')
 

    for url in soup.find_all('div',{"class":"job_seen_beacon"}):

        i = url.find('tbody') # go into table
        a = i.find('tr') # go further into table
        
        
        # gets job title
        for j in a.find_all('h2',{'class': 'jobTitle jobTitle-color-purple jobTitle-newJob'}):
          job_title = j.find_all('span')[1].get_text()
          print(job_title)
          
        # gets company name  
        
        for c in a.find_all('pre'):
          company = c.find_all('span')[0].get_text()
          print(company) 
        
        #gets company location

        company_location = c.find_all('div')[0].get_text()
        print(company_location)
        