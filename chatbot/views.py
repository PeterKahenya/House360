from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View


class ChatbotView(View):
    def get(self, request):
        return render(request,"chatbot.html",None,None)
    
    def post(self, request):
        return HttpResponse("Post Chatbot")
