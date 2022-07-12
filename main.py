import re

import requests
import bs4

website = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = bs4.BeautifulSoup(website.text, 'html.parser')
print(soup.prettify())
#------------------------------------------------------------------

# Task 1 - Scraper the Area of each country into a list
print('\n' '\n' '--- Task 1 ---')

country_area = []

areas = soup.find_all('span', class_='country-area')

for area in areas:
    c_area = area.text
    country_area.append(c_area)

print(country_area)
#------------------------------------------------------------------

# Task 2 - Scrape and print the first hyperlink on the site
print('\n' '\n' '--- Task 2 ---')

test = soup.find('a', class_="data-attribution")
print(test.get('href'))
#------------------------------------------------------------------

# Task 3 - Scrape and print the copyright text at the bottom of the site
print('\n' '\n' '--- Task 3 ---')

copyright = soup.find('div', class_='col-md-12 text-center text-muted')
print(copyright.text.strip())
#------------------------------------------------------------------
# Task 4 - How many items are in the 'row' class
print('\n' '\n' '--- Task 4 ---')

class_row = soup.find('div', class_='row')
print(len(class_row))

#------------------------------------------------------------------
# Task 5 - Scrape and print the capital of all countries that start with the letter 'e'
print('\n' '\n' '--- Task 5 ---')

all_countries = soup.find_all('div', class_="col-md-4 country")

for country in all_countries:
    country_name = (country.h3.text.strip())
    if country_name.startswith("E"):
        capital = country.find(class_="country-capital").text
        print(f"Country: {country_name} | Capital: {capital}")

#------------------------------------------------------------------
# Task 6 - Scrape and print data for Ghana only
print('\n' '\n' '--- Task 6 ---')

countries = soup.find_all('div', class_="col-md-4 country")

for info in countries:
    country = (info.h3.text.strip())
    if country == ("Ghana"):
        capital = info.find(class_="country-capital").text
        population = info.find(class_="country-population").text
        area = info.find(class_="country-area").text
        print(f" Capital {capital}, Population: {population}, Area: {area}")


#------------------------------------------------------------------
# Task 7 - Scrape and print the capitals that start with the letter 'b'
print('\n' '\n' '--- Task 7 ---')

all_capitals = soup.find_all('span', class_="country-capital")

for capitals in all_capitals:
    capital_name = (capitals.text.strip())
    if capital_name.startswith("B"):
        print(f"{capital_name}")