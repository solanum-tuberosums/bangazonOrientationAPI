from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.utils import timezone
from bangazon.api.models import *
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


import json


@csrf_exempt
def get_order(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object

    Author: Blaise Roberts
    '''
    req_body = json.loads(request.body.decode())
    token = req_body['token']
    token_instance = Token.objects.get(key=token)
    order = Order.objects.get_or_create(customer_id=token_instance.user, payment_type_id=None, order_date=timezone.now())
    data = json.dumps({"order":order[0].id})

    return HttpResponse(data, content_type='application/json')
