import requests
from bs4 import BeautifulSoup

#TODO
#charlotte region only on zillow pages
#find pages ending limit - usually 3 of number - or finding if the button doesnt exist

url = 'https://www.zillow.com/homes/for_sale/{}_p/'
page_num = 1

while True:
    response = requests.get(url.format(page_num))
    soup = BeautifulSoup(response.text, 'html.parser')

    houses = soup.find_all(class_='list-card-info')
    if not houses:
        break
    for house in houses:
        print(house.find(class_='list-card-title').text)

    page_num += 1

#within each house url find the supposed rental property price as well

house_urls = [
    'https://www.zillow.com/homedetails/123-Main-St-Anytown-USA-12345/12345678_zpid/',
    'https://www.zillow.com/homedetails/456-Park-Ave-Anytown-USA-67890/87654321_zpid/',
    # etc.
]

for url in house_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rental_income = soup.find(class_='rent-data-value')
    if rental_income:
        print(rental_income.text)
    else:
        print("Rental income not found for this property.")


# save all results and concat later on to list for pandas dataframe 

#export dataset into csv or google sheets for streamlit to access as an API

