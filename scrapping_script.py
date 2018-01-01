#### PULL QUOTES FROM GOODREADS ####
#Load dependencies
from bs4 import BeautifulSoup as bs
import urllib3 as url
import time
import csv
from langdetect import detect
url.disable_warnings()

def get_webpage(page_num):
    """Use urllib and BeautifulSoup to load webpage"""
    http = url.PoolManager()
    page = 'https://www.goodreads.com/author/quotes/17212.Marcus_Aurelius?page={}'.format(page_num)
    response = http.request('GET', page)
    soup = bs(response.data, "lxml")
    #return BeautifulSoup object
    return soup

#Loop through pages 1 to 20 and load pages into list
goodreads_quotes = []
for n in range(20):
    goodreads_quotes.append(get_webpage(n))
    time.sleep(5)

#Quotes are kept in divs with quoteText class
#Load quote divs
quote_divs = []
for page in goodreads_quotes:
    quote_divs.append(page.findAll("div", {"class": "quoteText"}))

#Get quotes from the div, remove quotation marks and space characters that prefix quote
quote_text = [q.text.split("\n")[1][6:] for div in quote_divs for q in div]
quote_text = [q[1:len(q)-1] for q in quote_text]

#Some quotes are not english, remove all non-english quotes using langdetect library
english_quotes = [q for q in quote_text if detect(q) == 'en']

#Save quotes to csv file
with open("quotes.csv", "w") as file:
    writer = csv.writer(file, delimiter="/")
    writer.writerow(english_quotes)
