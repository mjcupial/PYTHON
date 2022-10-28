'''

http://quotes.toscrape.com
'''
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import writer, DictWriter

BASE_URL = "http://quotes.toscrape.com"
def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        print(f"Scraping {BASE_URL}{url}...")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio": quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(1)    #--> do not overload the server in each requests, be polite and set sleep
    return all_quotes
def write_quotes(quotes):
    with open("quotes.csv", "w") as file:
        headers = ["text", "author", "bio"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)