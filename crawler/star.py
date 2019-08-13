from bs4 import BeautifulSoup
import requests
import datetime
import urllib
from django.conf import settings
import os
from properties.models import Property


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
            price = verify(section.find('div', {'class': 'product-price'}))
            location = verify(section.find('p', {'class': 'product-top-meta'}))
            description = verify(section.find('p', {'class': 'product-description'}))
            bathroom = verify(section.find('div', {'class': 'real_estate__number_of_bathrooms'}))
            bedroom = verify(section.find('div', {'itemprop': 'numberOfRooms'}))
            area = verify(section.find('div', {'itemprop': 'floorSize'}))
            link = section.find('a', {'class': 'product-link js_product-link'}).get('href')
            path = os.path.join(settings.MEDIA_ROOT, "images/"+str(datetime.datetime.now().microsecond) + ".jpg")
            resource = urllib.request.urlopen(image)
            output = open(path, "wb")
            output.write(resource.read())
            output.close()

            property.path = link
            property.image_url = image
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
