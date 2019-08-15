from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from properties.models import Property
from django.db.models import Q


class HomeView(View):
    def get(self, request):
        properties = Property.objects.all()
        locations=Property.objects.order_by().values('location').distinct()
        return render(request, 'home.html', {'properties': properties,'locations':locations}, None)

    def post(self, request):
        term = request.POST['term']
        properties = Property.objects.filter(Q(title__icontains=term)|Q(description__icontains=term))
        return render(request, "home.html", {'properties': properties}, None)
