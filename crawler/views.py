from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View
from .star import crawl_house



class CrawlerView(View):
    def get(self, request):
        return render(request,"crawler.html",None,None)
    
    def post(self, request):
        url=request.POST['url'] or "https://www.the-star.co.ke/classifieds/house-apartment-for-rent/house--nairobi"
        site=request.POST['site']
        # decide which crawler to use
        print(url)
        result=crawl_house(url)

        with open("star.json","w") as f:
            f.write(str(crawl)) 
            return HttpResponse("Crawler Done")
        return HttpResponse("Post Crawler")
