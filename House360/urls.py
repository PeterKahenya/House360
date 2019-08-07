from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView
from crawler.views import CrawlerView
from chatbot.views import ChatbotView
from insights.views import InsightsView
from properties.views import PropertiesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('properties', PropertiesView.as_view()),
    path('insights', InsightsView.as_view()),
    path('chatbot', ChatbotView.as_view()),
    path('crawler', CrawlerView.as_view()),
]