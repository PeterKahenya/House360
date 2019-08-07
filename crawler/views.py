from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View


class CrawlerView(View):
    def get(self, request):
        return HttpResponse("Get Crawler")
    
    def post(self, request):
        return HttpResponse("Post Crawler")
