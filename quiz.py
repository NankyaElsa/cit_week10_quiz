"""
1.Scrape CBS news https://www.cbsnews.com/latest/rss/main and get the following data

Title
Link
Image
description
Using SqlAlchemy create a table called cbs_news and insert the data into the table.

Implement one route called /cbs_news that returns the data in json format.

NOTE: Use lxml to parse the xml data.
"""
import requests
from bs4 import BeautifulSoup


url="https://www.cbsnews.com/latest/rss/main"
page=requests.get(url)
soup=BeautifulSoup(page.text, features="xml")
#print(soup.prettify())

# item=soup.find("item")
# print(item)

# title=item.find("title").text
# print(title)
# link=item.find("link").text
# print(link)
# image=item.find("image").text
# print(image)
# description=item.find("description").text
# print(description)

items=soup.find_all("item")
cbs_news=[]
for item in items:
    title=item.find("title").text
    link=item.find("link").text
    image=item.find("image").text
    description=item.find("description").text
    cbs_news.append(f"title{title} link{link} image{image} description{description}")
print(cbs_news)
    






