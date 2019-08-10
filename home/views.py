from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request,'home.html',{'common':[1,2,3,4,5]},None)
    
    def post(self, request):
        return HttpResponse("Post Homepage")
