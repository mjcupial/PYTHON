'''

http://quotes.toscrape.com
'''
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_url="http://quotes.toscrape.com"
url = "/page/1"

while url:
    res = requests.get(f"{base_url}{url}")
    print(f"Scraping {base_url}{url}...")
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
    # sleep(2)    # --> do not overload the server in each requests, be polite

#### THE GAME LOGIC ####
quote = choice(all_quotes)
remaining_guesses = 4
print("Here is a quote: " + quote["text"])
print(quote["text"] + quote["author"])
guess = ''
while guess.lower() != quote["author"].lower():
    guess = input(f"Who said this quote? Guess remaining: {remaining_guesses}")
print("AFTER WHILE LOOP")