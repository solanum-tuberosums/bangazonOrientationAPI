from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.utils import timezone
import json

def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object

    Author: Beve Strownlee
    '''

    # Obtain the context for the user's request.
    context = RequestContext(request)
    req_body = json.loads(request.body.decode())


    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        
        # Use the built-in authenticate method to verify
        username=req_body['username']
        password=req_body['password']

        print("\n\n{}\n\n".format(username))
        print("\n\n{}\n\n".format(password))

        authenticated_user = authenticate(username=username, password=password)

        print("\n\n{}\n\n".format(authenticated_user))

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('/')

        else:
            # Bad login details were provided. So we can't log the user in.
            return HttpResponse("Invalid login details supplied.")


        return render(request, 'login.html', {}, context)
    elif request.method == 'GET':
        login_form = LoginForm()
        template_name = "login.html"
        return render(request, template_name, {"login_form":login_form})