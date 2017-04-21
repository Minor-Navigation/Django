# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from models import Users


def req(request):
    	return JsonResponse({'foo':'bar'})

def index(request):
    return HttpResponse("Hello, world")

def detail(request, id):
    return HttpResponse("You're looking at question %s." % id)

def results(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id)

def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)    
  
