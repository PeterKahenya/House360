from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View


class ChatbotView(View):
    def get(self, request):
        return HttpResponse("Get Chatbot")
    
    def post(self, request):
        return HttpResponse("Post Chatbot")
