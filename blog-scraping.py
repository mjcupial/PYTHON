'''
Let's scrape data into CSV!
goal: grab all links from Rithm School blog [https://www.rithmschool.com/blog]
data: store URL, anchor tag text, and date
'''
import requests
from bs4 import BeautifulSoup
from csv import writer

pages = soup.find_all(class_="page")
print(pages)
# for page in pages:
#     response = requests.get("https://www.rithmschool.com/blog")
#     # print(response.text)
#     soup = BeautifulSoup(response.text, "html.parser")
#     articles = soup.find_all("article")
#     # print(articles)
#     page = soup.find_all("")
#
#     with open("blog_data.csv", "w") as csv_file:
#         csv_writer = writer(csv_file)
#         csv_writer.writerow(["title", "link", "date"])
#         for article in articles:
#             a_tag = article.find("a")
#             title = a_tag.get_text()
#             url = a_tag["href"]
#             date = article.find("time")["datetime"]
#             # print(f"{title} | {url} | {date}")
#             csv_writer.writerow([title,url,date])
