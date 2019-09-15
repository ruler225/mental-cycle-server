from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json

# Create your views here.
def register_user(request):
    #get new user details from POST
    userinfo = request.POST
    uname = userinfo.get('username', '')
    passwd = userinfo.get('password', '')

    #check if anything is empty
    if uname == '':
        return HttpResponse('Username cannot be empty!')
    elif passwd == '':
        return HttpResponse('Password cannot be empty!')

    #check if username already exists
    if User.objects.all().filter(username=uname).count() > 0:
        return HttpResponse("That username is already taken")
    
    User.objects.create_user(username=uname, password=passwd)
    return HttpResponse('Success')

def login_user(request):

    #get user credentials from POST
    credentials = request.POST 
    uname = credentials.get('username', '')
    passwd = credentials.get('password','')

    user = authenticate(request, username=uname, password=passwd)

    #check if authentication succeeded
    if user is not None:
        login(request,user)
        return HttpResponse('Success')
    else:
        return HttpResponse('Login failed')

def logout_user(request):
    logout(request)
    return HttpResponse('Logged Out')
