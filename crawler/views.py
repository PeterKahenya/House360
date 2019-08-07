from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View


class CrawlerView(View):
    def get(self, request):
        return render(request,"crawler.html",None,None)
    
    def post(self, request):
        return HttpResponse("Post Crawler")
