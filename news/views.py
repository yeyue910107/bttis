# Create your views here.
from bttis.news.models import List
from bttis.news.models import Item
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def display(request, offset):
    news_id = int(offset)
    news = Item.objects.get(id = news_id)
    return render_to_response('news/news.html', {'news':news})