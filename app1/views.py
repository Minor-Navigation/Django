# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models import Users

import json

import os


@csrf_exempt
def req(request):
    i=0;
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'data.txt')
    list1=[]
    with open(file_path) as fp:
        for line in fp:
            words = line.split(" ") 
            #loc = {'lat':float(words[0]),  'lon': float(words[1]) }
            list1.append(float(words[0]))
            list1.append(float(words[1]))

            i+=1
            if(i==100000):
                break;
    
    print list1            
    print(request.POST.get('search_name'))
    #list1 = ['physics', 'chemistry', 1997, 2000];
    context = {'list': list1}

    return render(request, 'view1.html', context)

    #return JsonResponse({'foo':'bar'})

def index(request):
    return HttpResponse("Hello, world")

def detail(request, id):
    return HttpResponse("You're looking at question %s." % id)

def results(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id)

def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)    
  
@csrf_exempt
def signup(request):
    #return JsonResponse({'foo':'bar'})
    #print(request.body.get('name'))
    #print(request.get_json())


    print(request.body)   
    data = json.loads(request.body)

    print(data['name'])
    # {"email":"a","password":"a","name":"a","address":"a"}

    # #s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
    # json_acceptable_string = (request.body).replace("'", "\"")
    # d = json.loads(request.body)
    # print(d)
    # print(d.name)

    #print("post=", request.POST)
	
    returnRespone = {}
    returnRespone['error'] = "1"
    # print(request.POST.get('flat'),request.POST.get('flong'),request.POST.get('dlat'),request.POST.get('dlong'))

    #if (request.method=='POST' and  not( request.POST.get('name')=='' or request.POST.get('email')==''  or request.POST.get('password')=='' or request.POST.get('address')=='') )  :
    if (request.method=='POST' and  not( data['name']=='' or data['email']==''  or data['password']=='' or data['address']=='') )  :
        print ("Got the post req")
        # user = Users(
        #     name=str(request.POST.get('name')),
        #     password=str(request.POST.get('password')),
        #     email=str(request.POST.get('email')),
        #     address=str(request.POST.get('address')),
        #     )
        user = Users(
            name=str(data['name']),
            password=str(data['password']),
            email=str(data['email']),
            address=str(data['address']),
            )
        user.save()
        returnRespone['error'] = "0"
        return JsonResponse(returnRespone)
    else:
        return JsonResponse(returnRespone)
     

@csrf_exempt
def login(request):
    
    print(request.body)   
    data = json.loads(request.body)
    #if (request.method=='POST' and  not( request.POST.get('email')==''  or request.POST.get('password')=='' ) ) :
    if (request.method=='POST' and  not( data['email']==''  or data['password']==''))  :
    
        
        print(request)
        print(data['email'])
        print(data['password'])
        email=str(data['email'])
        password=str(data['password'])
        
        dataToBeSend = {}
        dataToBeSend['login_value'] = 'not ok'
        dataToBeSend['error'] = "1"

        if(Users.objects.filter(password=password, email=email).exists()):
            request.session['email'] = email
            email=request.session['email']
            user=(Users.objects.get(email=email))
            
            
            name=user.name
            print ("name=", name)
            dataToBeSend['name'] =str(name)
            dataToBeSend['login_value'] = 'ok'
            dataToBeSend['error'] = "0"
            print (JsonResponse(dataToBeSend))
            return JsonResponse(dataToBeSend)

        else:
            print (JsonResponse(dataToBeSend))
            return JsonResponse(dataToBeSend)
    else:
        return JsonResponse({'error':"1"})        

@csrf_exempt
def logout(request):
    print request
    try:
        print request.session._session_key
        print request.session.items()
        del request.session['email']
        print request.session.items()
        return JsonResponse({'error':0})
    except:
        return JsonResponse({'error':1})
    
