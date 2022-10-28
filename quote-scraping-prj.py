'''

http://quotes.toscrape.com
'''
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_url="http://quotes.toscrape.com"
url = "/page/1/"

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
    sleep(2)    #--> do not overload the server in each requests, be polite

#### THE GAME LOGIC ####
quote = choice(all_quotes)
remaining_guesses = 4
print("Here is a quote: " + quote["text"])
print(quote["text"] + quote["author"]) #-->  hint
guess = ''
while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    guess = input(f"Who said this quote? Guess remaining: {remaining_guesses}  -> ")
    if guess.lower() == quote["author"].lower():
        print("YOU GOT IT RIGHT!")
        break
    remaining_guesses -= 1
    if remaining_guesses == 3:
        res = requests.get(f"{base_url}{quote['bio']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"Here's a hint: The author was born {birth_place} | {birth_date}")
    elif remaining_guesses == 2:
        print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[1][0]
        print(f"Here's a hint: The author's last name starts with: {last_initial}")
    else:
        print(f"Sorry you ran out of guesses. The answer was {quote['author']}")
print("End of the game")