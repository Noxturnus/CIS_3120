import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

#Send HTTP GET Request
response = requests.get(url, timeout = 20)
response.raise_for_status()

#Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

#Find all the laptops product containers
products = soup.find_all("div", class_="thumbnail")

if not products:
    raise ValueError("No Products Found. Check teh Website and HTML selectors!!")

names = []
prices = []

#Extract Laptop name 
for product in products:
    name_tag = product.find("a", class_="title")
    price_tag = product.find("h4", class_ = "price")

    if name_tag and price_tag:
        names.append(name_tag.get_text(strip=True))
        prices.append(price_tag.get_text(strip=True))

#Create the DataFrame
data = pd.DataFrame({"Laptop":names, "Price":prices})
print(data)

#Save the data to CSV
data.to_csv("laptops.cvs", index = False)
print("------------------------------")
print("Data Scrapped Successfuly and Saved to Laptops.csv")