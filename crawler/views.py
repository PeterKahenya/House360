from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .star import crawl_house
import json


class CrawlerView(View):
    def get(self, request):
        return render(request, "crawler.html", None, None)

    def post(self, request):
        url = request.POST['url'] or "https://www.the-star.co.ke/classifieds/house-apartment-for-rent/house--nairobi"
        site = request.POST['site']
        crawl_house(url)
        return render(request, "crawler.html", None, None)
