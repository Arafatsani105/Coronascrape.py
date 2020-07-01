import requests #all this module are required.
from bs4 import BeautifulSoup  #all this module are required.

country = input(
    "Country Name : ")
scraper_website = requests.get(
    "https://www.worldometers.info/coronavirus/country/" + country)
soup = BeautifulSoup(scraper_website.content, 'html.parser')

item = soup.find(id='page-top').get_text()
cases = soup.find(class_='maincounter-number').get_text()
recovered = soup.find(
    class_='maincounter-number', style="color:#8ACA2B ").get_text()

print(item)
print("Corona Cases:"+cases)
print("People who recovered  :" + recovered)
