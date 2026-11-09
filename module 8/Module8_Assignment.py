#Set Up the Environment
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Identify the Website to Scrape
url = "https://realpython.github.io/fake-jobs/"

#Download the Web Page
response = requests.get(url)
response.raise_for_status()

#Parse the HTML Content
soup = BeautifulSoup(response.text, "html.parser")

#Find all the job containers
jobs = soup.find_all("div", class_="media-content")

job_title = []
company_name = []

#Extract jobs name 
for job in jobs:
    title = job.find("h2", class_="title is-5").text
    company = job.find("h3", class_="subtitle is-6 company").text

    job_title.append(title)
    company_name.append(company)

#Create the DataFrame
data = pd.DataFrame({"Title":job_title, "Company":company_name})
print(data)

#Save the data to CSV
data.to_csv("jobs.csv", index = False)
print("------------------------------")
print("Data Scrapped Successfuly and Saved to jobs.csv")