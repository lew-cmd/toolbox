# pylint: disable=missing-module-docstring

import sys
#import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"

def search_city(query):
    '''Look for a given city and disambiguate between several candidates.
    Return one city (or None)'''
    url = f"https://www.metaweather.com/api/location/search/?query={query}"
    response=requests.get(url).json()
    if len(response) < 1:
        print("URL loading failed, city does not exist")
        return None
    city = response[0]
    return city

def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''
    url = f"https://www.metaweather.com/api/location/{woeid}"
    response = requests.get(url).json()
    
    if len(response) < 1:
        print("URL loading failed, WOEID does not exist")
        return None
    
    weather = response["consolidated_weather"]
    
    return weather

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    print(city)
    
    woeid = city["woeid"]
    weather = weather_forecast(woeid)
    
    print("The weather in " + city["title"] + " for the next 5 days:")
    
    for item in weather[1:]:
        print(f"{item['applicable_date']}: {item['weather_state_name']} {round(item['max_temp'])}°C")
        
if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
