from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('main/index.html')

def main(request):
    return render_to_response('main/main.html')

def top(request):
    return render_to_response('main/top.html')

def foot(request):
    return render_to_response('main/foot.html')