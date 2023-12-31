from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    articles = NewsArticle.objects.all()  # Fetch all articles from the database
    return render(request, 'news/home.html', {'articles': articles})