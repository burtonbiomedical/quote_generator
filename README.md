# Marcus Aurelius Quote Generator

This is a small web application I created for my own practice as part of
my on-going study with FreeCodeCamp.
The app generates quotes from Marcus Aurelius, obtained from www.goodreads.com.

Using Python 3.5 and the libraries BeautifulSoup 4 and Urllib3, I scrapped the site
for quotations and formated for future use, before saving the contents to a CSV file.

The HTML page, styled using the Bootstrap CSS library, employs Javascript, JQuery and
AJAX to load the contents of the CSV file and generates a new random quote when the
user clicks the "New Quote" button. The page also features a 'tweet' button, which
checks the quote meets Twitters character limitations before navigating the user
to Twitter with the quote preloaded.
