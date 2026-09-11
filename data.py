from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://in.indeed.com/jobs?q=python&l=&from=searchOnHP')
soup = BeautifulSoup(html_text.text, 'html.parser')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
    skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
    published_date = job.find('span', class_= 'sim-posted').span.text
    print(published_date)

    print(f'''
    Company Name: {company_name}
    Required Skills: {skills}
    ''')

    print('')