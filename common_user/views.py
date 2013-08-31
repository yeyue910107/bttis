# Create your views here.
from bttis.common_user.models import CommonUser
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def logindex(request):
    if 'userName' in request.session:
        userName = request.session['userName']
        return render_to_response('common_user/index.html', {'userName':userName})
    else:
        return render_to_response('common_user/login.html')

def reg(request):
    return render_to_response('common_user/register.html')

def login(request):
    userName = request.POST['userName']
    password = request.POST['password']
    #print username, password
    user = CommonUser.objects.filter(userName = userName, password = password)
    #user = CommonUser(userName = username, password = password)
    #if user in CommonUser.objects.all():
    if user:
        request.session['userName'] = userName
        return render_to_response('common_user/index.html', {'userName':userName})
    else:
        return render_to_response('common_user/login_error.html')

def logout(request):
    try:
        del request.session['userName']
    except KeyError:
        pass
    return render_to_response('common_user/login.html')

def register(request):
    username = request.POST['userName']
    password = request.POST['password']
    newuser = CommonUser(userName = username, password = password)
    newuser.save()
    return render_to_response('common_user/register_success.html')

def password(request):
    return render_to_response('common_user/password.html')

def set_password(request):
    userName = request.session['userName']
    password = request.POST['newpassword1']
    user = CommonUser.objects.get(userName = userName)
    user.password = password
    user.save()
    return render_to_response('common_user/password_success.html')