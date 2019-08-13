from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from properties.models import Property


class HomeView(View):
    def get(self, request):
        properties = Property.objects.all()
        return render(request, 'home.html', {'properties': properties}, None)

    def post(self, request):
        properties = Property.objects.all()
        render(request, 'home.html', {'properties': properties}, None)
