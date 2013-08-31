# Create your views here.
from bttis.train.models import Train
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import list_detail
from django.db.models import Q

def index(request):
    return render_to_response('train/train_query.html')

def query_station_station(request):
    startStation = request.GET['startStation']
    destination = request.GET['destination']
    #train_list = Train.objects.filter(startStation = startStation, endStation = endStation)
    return list_detail.object_list(
        request,
        queryset = Train.objects.filter(startStation = startStation, destination = destination),
        paginate_by = 1,
        template_name = "train/query_result1.html",
        extra_context= {
            'startStation':startStation,
            'destination':destination,
            }
    )
    #return render_to_response('train/query_result1.html', {'train_list':train_list})

def query_trainNum(request):
    trainNum = request.GET['trainNum']
    #trains = Train.objects.all()
    train_list = Train.objects.filter(trainNum__iexact = trainNum)
    #print train_list[0].startStation
    return render_to_response('train/query_result2.html', {'train_list':train_list})

def query_station(request):
    station = request.GET['station']
    #trains = Train.objects.get(Q(startStation = station) | Q(endStation = station))
    return list_detail.object_list(
        request,
        queryset = Train.objects.filter(Q(startStation = station) | Q(destination = station)),
        paginate_by = 1,
        template_name = "train/query_result3.html",
        extra_context= {
            'station':station,
            }
    )