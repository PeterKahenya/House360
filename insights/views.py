from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View


class InsightsView(View):
    def get(self, request):
        return render(request,"insights.html",None,None)
    
    def post(self, request):
        return HttpResponse("Post Insights")
