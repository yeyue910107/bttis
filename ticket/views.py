# Create your views here.
from bttis.ticket.models import Ticket, TicketInfo, List
from bttis.train.models import Train
from bttis.common_user.models import CommonUser
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import list_detail
from django.db.models import Q

def post_step1(request):
    return render_to_response('ticket/post_step1.html')

def post_step2(request):
    infotype = request.POST['infotype']
    trainNum = request.POST['trainNum']
    tickettype = List.objects.all()
    return list_detail.object_list(
        request,
        queryset = Train.objects.filter(trainNum__iexact = trainNum),
        template_name = "ticket/post_step2.html",
        extra_context= {
            'infotype':infotype,
            'trainNum':trainNum,
            'tickettype':tickettype,
            }
    )

def post(request):
    userName = request.session['userName']
    infotype = request.POST['infotype']
    trainNum = request.POST['trainNum']
    startStation = request.POST['startStation']
    destination = request.POST['destination']
    tickettype = request.POST['type']
    ticketNum = request.POST['ticketNum']
    date = request.POST['date']
    phone = request.POST['phone']
    extraContext = request.POST['extraContext']
    list = List.objects.get(title = tickettype)
    user = CommonUser.objects.get(userName = userName)
    ticket = Ticket(trainNum = trainNum, startStation = startStation, destination = destination,
                    tickettype_id = list.id, date = date)
    ticket.save()
    ticket_info = TicketInfo(infotype = infotype, ticketNum = ticketNum, ticket_id = ticket.id,
                             phone = phone, extraContext = extraContext, user_id = user.id)
    ticket_info.save()
    return render_to_response('ticket/post_success.html')

def mypost(request):
    userName = request.session['userName']
    user = CommonUser.objects.get(userName = userName)
    print userName
    return list_detail.object_list(
        request,
        queryset = TicketInfo.objects.filter(user = user),
        template_name = 'ticket/mypost.html',
        extra_context = {
                'userName':userName,
            }
        )

def index(request):
    return render_to_response('ticket/ticket_query.html')

def query_station_station(request):
    startStation = request.GET['startStation']
    destination = request.GET['destination']
    return list_detail.object_list(
        request,
        queryset = TicketInfo.objects.filter(infotype = '转让', ticket__startStation = startStation, ticket__destination = destination),
        paginate_by = 1,
        template_name = "ticket/query_result1.html",
        extra_context= {
            'startStation':startStation,
            'destination':destination,
            }
    )

def query_trainNum(request):
    trainNum = request.GET['trainNum']
    return list_detail.object_list(
        request,
        queryset = TicketInfo.objects.filter(infotype = '转让', ticket__trainNum__iexact = trainNum),
        paginate_by = 10,
        template_name = "ticket/query_result2.html",
        extra_context= {
            'trainNum':trainNum,
            }
    )

def post_info(request, offset):
    info_id = int(offset)
    ticket_info = TicketInfo.objects.get(id = info_id)
    return render_to_response('ticket/post_info.html', {'ticket_info':ticket_info})

def mypost_info(request, offset):
    info_id = int(offset)
    ticket_info = TicketInfo.objects.get(id = info_id)
    return render_to_response('ticket/mypost_info.html', {'ticket_info':ticket_info})