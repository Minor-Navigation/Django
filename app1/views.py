# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models import Users

import json
import os
import example as e

@csrf_exempt
def req(request):
    i=0;
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'data.txt')
    list1=[]
    with open(file_path) as fp:
        for line in fp:
            i+=1
            # if(i%300000!=0):#change here for no. of nodes.
            #     continue;

            words = line.split(" ") 
            #loc = {'lat':float(words[0]),  'lon': float(words[1]) }
            list1.append(float(words[0]))
            list1.append(float(words[1]))

            
            if(i==100):#change here for no. of nodes.
                break;
    
    #print list1            
    #print(request.POST.get('search_name'))
    #list1 = ['physics', 'chemistry', 1997, 2000];
    context = {'list': list1}

    return render(request, 'view1.html', context)

    #return JsonResponse({'foo':'bar'})

@csrf_exempt
def return_list(request):
    print("request param= ", request.POST.get("search"))
    prefix=request.POST.get("search")

    response = {'name': [], 'id': []}
    names = []
    ids = []

    t=e.trie()
    #w=t.search_trie("Hapur Road")
    st=str(prefix)
    #print ("st=", st);

    t.display_prefix(st,len(st),0)
    for i in t.list:
        #print (i)
        ids.append(int(i))
    for i in t.prefix:
        #print (i)
        names.append(i)    

    t.close()
    response['name']=names
    response['id']=ids
    
    #print response
    #print JsonResponse(response)        

    #print(t.list[0])
    #print(t.prefix[0])
    
    return JsonResponse(response)

@csrf_exempt
def data(request):
    name=request.POST.get("name")
    t=e.trie()
    w=t.search_trie(name)
    print("w=",w.getid())
    t.close()
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
  

     
