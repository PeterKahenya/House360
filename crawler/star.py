from bs4 import BeautifulSoup
import requests
import datetime
import urllib

def verify(tag):
    if tag is not None:
        return tag.text
    else:
        return ""

def crawl_house(url):
     result = []
     req = requests.get(url)
     soup = BeautifulSoup(req.text, "lxml")
     all_sections = soup.find_all('section',{'class':'property'}) 
    
     for section in all_sections:
        try:
            house_dict = {}
            title=verify(section.find('h2',{'class':'product-title'}))
            image="https:"+section.find('img',{'class':'image_List'}).get("data-src")
            price=verify(section.find('div',{'class':'product-price'}))
            location=verify(section.find('p',{'class':'product-top-meta'}))
            description=verify(section.find('p',{'class':'product-description'}))
            bathroom=verify(section.find('div',{'class':'real_estate__number_of_bathrooms'}))
            bedroom=verify(section.find('div',{'itemprop':'numberOfRooms'}))
            area=verify(section.find('div',{'itemprop':'floorSize'}))
            
            link=section.find('a',{'class':'product-link js_product-link'}).get('href')
            

            path="images/"+str(datetime.datetime.now().microsecond)+".jpg"
            resource = urllib.request.urlopen(image)
            output = open(path,"wb")
            output.write(resource.read())
            output.close()

            house_dict["path"]=path
            house_dict["title"]=title
            house_dict["price"]=float(price.strip(" KSh ").replace(',',''))
            house_dict["location"]=location
            house_dict["description"]=description
            house_dict["bathroom"]=bathroom
            house_dict["bedroom"]=int(bedroom.strip(" bedroom(s)"))
            house_dict["area"]=area
            house_dict["link"]=link
            #print(house_dict)
            result.append(house_dict)
        except Exception as e:
            print("exception occurred , continuing",e)
            continue
        

     return result

url = 'https://www.the-star.co.ke/classifieds/house-apartment-for-rent/house--nairobi'
crawl  = crawl_house(url)
with open("star.json","w") as f:
    f.write(str(crawl)) 
