#Set Up the Environment
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Identify the Website to Scrape
url = "http://books.toscrape.com/"

#Download the Web Page
response = requests.get(url)
response.raise_for_status() #Optional for errors

#Parse the HTML Content
soup = BeautifulSoup(response.text, "html.parser")


#Find all the laptops book containers
books = soup.find_all("article", class_="product_pod")

titles = []
prices = []

#Extract books name 
for book in books:
    title = book.h3.a['title']
    price = book.find("p", class_ = "price_color").text

    titles.append(title)
    prices.append(price)

#Create the DataFrame
data = pd.DataFrame({"Title":titles, "Prices":prices})
print(data)

#Save the data to CSV
data.to_csv("books.csv", index = False)
print("------------------------------")
print("Data Scrapped Successfuly and Saved to Books.csv")