INST 326 Project 8-Job Finder

Professor Gabriel Cruz

Group members: Arifun Nabi, David Mejias, Keyun Liu

Project Instruction:

This project's function it to scrape the data about job title of user's selection from Indeed website. We pre-entered Data Scientist for testing. It can be changed in "if __name__ "function.  
·It will scrap the related jot title, the company name, the data of published, salary, and address,etc.  
·Then the data will be extract as a csv file.  
·Finally the csv file will be send to email. The feature is set to send a email to the email filled itself. In the demo we used a new created gmail for testing.

Before you run the code:  
You will need to install following modules   

request  
BeautifulSoup  
mimetypes  
datetime  
pandas  
smtplib  
csv  
