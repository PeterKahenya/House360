from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View
from properties.models import Property
from django.core import serializers
from django.http.response import JsonResponse
from django.db.models import Count
import json



class InsightsView(View):
    def get(self, request):
        return render(request,"insights.html",None,None)
    
    def post(self, request):
        return HttpResponse("Post Insights")

class QueriesView(View):
    def get(self, request,query):
        results=Property.objects.values('location').annotate(counts=Count('location'))
        return JsonResponse(list(results),safe=False)
    
    def post(self, request):
        return HttpResponse("Post Insights")