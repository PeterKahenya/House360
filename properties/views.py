from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View


class PropertiesView(View):
    def get(self, request):
        return render(request,"properties.html",None,None)
    
    def post(self, request):
        return HttpResponse("Post Properties")
