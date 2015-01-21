from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import urllib
from django.http import HttpResponseRedirect
import json
#from oautherise.forms import Userform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        # user_form = User(data=request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        #userprofile_form = UserProfileForm(data=request.POST)
        if username and email and password:
            user = User.objects.create_user(username, email, password)
            user.save()

            registered =True
            user = authenticate(username=username, password=password)

            login(request, user)
            return HttpResponseRedirect('/')

        else:
            print user_form.errors
    else:
        user_form = User()
        # userprofile_form = UserProfileForm()

    return render_to_response('register.html', {'user_form': user_form, 'registered': registered}, context)
# Create your views here.

def user_login(request):

    context = RequestContext(request)


    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)


        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")


    else:
        return render_to_response('login.html', {}, context)

@login_required
def user_logout(request):

    logout(request)


    return HttpResponseRedirect('/')

