from bs4 import BeautifulSoup
import requests
import datetime
import urllib
from django.conf import settings
import os
import re
from properties.models import Property

def extract_value(val):
    x=re.findall(r'\d+', val.replace(',',''))
    if x:
        return x[0]
    return 0 

def verify(tag):
    if tag is not None:
        return tag.text
    else:
        return ""


def crawl_house(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    all_sections = soup.find_all('section', {'class': 'property'})
    for section in all_sections:
        property = Property()
        try:
            title = verify(section.find('h2', {'class': 'product-title'}))

            image = "https:"+section.find('img', {'class': 'image_List'}).get("data-src")

            price = extract_value(verify(section.find('div', {'class': 'product-price'})))

            location = verify(section.find('p', {'class': 'product-top-meta'}))

            description = verify(section.find('p', {'class': 'product-description'}))

            bathroom = extract_value(verify(section.find('div', {'class': 'real_estate__number_of_bathrooms'})))

            bedroom = extract_value(verify(section.find('div', {'itemprop': 'numberOfRooms'})))

            area = extract_value(verify(section.find('div', {'itemprop': 'floorSize'})))

            link = section.find('a', {'class': 'product-link js_product-link'}).get('href')
            
            specific=str(datetime.datetime.now().microsecond) + ".jpg"
            path =os.path.join(os.path.join(settings.MEDIA_ROOT, 'images'),specific)
            resource = urllib.request.urlopen(image)
            output = open(path, "wb")
            output.write(resource.read())
            output.close()

            property.path = link
            property.image_url = specific
            property.title = title
            property.price = price
            property.location = location
            property.description = description
            property.bathroom = bathroom
            property.bedroom = bedroom
            property.area = area
            property.save()
        except Exception as e:
            print("exception occurred , continuing",e)
            continue

if __name__ == '__main__':
    url = 'https://www.the-star.co.ke/classifieds/house-apartment-for-rent/house--nairobi'
    crawl = crawl_house(url)
    with open("star.json", "w") as f:
        f.write(str(crawl))
