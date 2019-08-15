from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from properties.models import Property
from django.db.models import Q


class HomeView(View):
    def get(self, request):
        properties = Property.objects.all()
        return render(request, 'home.html', {'properties': properties}, None)

    def post(self, request):
        term = request.POST['term']
        properties = Property.objects.filter(Q(title__icontains=term)|Q(description__icontains=term))
        return render(request, "home.html", {'properties': properties}, None)
