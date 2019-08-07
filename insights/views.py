from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View


class InsightsView(View):
    def get(self, request):
        return HttpResponse("Get Insights")
    
    def post(self, request):
        return HttpResponse("Post Insights")
