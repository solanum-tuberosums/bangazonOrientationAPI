from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from bangazon.api.views.login_user_view import login_user
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    )

    # Commit the user to the database by saving it
    new_user.save()
    token = Token.objects.create(user=new_user)
    data = json.dumps({'token':token.key})

    return HttpResponse(data, content_type='application/json')
