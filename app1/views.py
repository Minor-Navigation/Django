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

################################################################

#for page initial loading 
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

################################################################

#for  returning list of prefix
@csrf_exempt
def return_list(request):
    print("request param= ", request.POST.get("search"))
    prefix=request.POST.get("search")

    response = {'way_names': [], 'way_ids': [],'node_names': [], 'node_ids': [],  }
    way_names = []
    way_ids = []
    node_names = []
    node_ids = []


    t=e.trie()
    #w=t.search_trie("Hapur Road")
    st=str(prefix)
    #print ("st=", st);

    t.display_prefix(st,len(st),0)
    for i in t.list:
        #print (i)
        way_ids.append(int(i))
    for i in t.prefix:
        #print (i)
        way_names.append(i)


    t.display_prefix_node(st,len(st),0)
    for i in t.list:
        #print (i)
        node_ids.append(int(i))
    for i in t.prefix:
        #print (i)
        node_names.append(i)        

    t.close()
    response['way_names']=way_names
    response['way_ids']=way_ids
    response['node_names']=node_names
    response['node_ids']=node_ids
    
    #print response
    #print JsonResponse(response)        

    #print(t.list[0])
    #print(t.prefix[0])
    
    return JsonResponse(response)
################################################################

#for returning info of selected name. 
@csrf_exempt
def data(request):
    way_list=[]    #longlat list
    dlist=[]   #delimiter list
    node_list=[]
    response = {'way_list': [], 'dlist': [], 'node_list':[], 'type': "none"}
    
    name=request.POST.get("name")
    
    t=e.trie()
    w=t.search_trie(name)
    n=t.search_trie_node(name)
    #print("w=",w.getid())
    print("w=",w.wayptr)

    if(n.nodeptr >= 0):
        t.node_with_nodeid(n.nodeptr)
        for i in t.lat_list:
            node_list.append(float(i))

    if(n.nodeptr >= 0):
        t.node_with_wayid(w.wayptr)
        for i in t.lat_list:
            #print (i)
            way_list.append(float(i))
        for i in t.delimiter_list:
            #print (i)
            dlist.append(float(i))
        
    
    print("lat=", t.lat_list, "\ndlist=", t.delimiter_list)
    print("nodelist", node_list)

    #response['long']=t.long_list
    response['way_list']=way_list
    response['dlist']=dlist
    response['node_list']=node_list


    
    t.close()
    return JsonResponse(response)


################################################################

#for returning rtree. 
@csrf_exempt
def rtree(request):
    
    admin_level=request.POST.get("admin_level")
    minLat=request.POST.get("minLat")
    minLon=request.POST.get("minLon")
    maxLat=request.POST.get("maxLat")
    maxLon=request.POST.get("maxLon")
    print("rtree",admin_level, minLat, minLon,maxLat, maxLon)
    return JsonResponse({'foo':'bar'})

################################################################

#for returning shortest path. 
@csrf_exempt
def astar(request):
    
    Lat1=request.POST.get("Lat1")
    Lon1=request.POST.get("Lon1")
    Lat2=request.POST.get("Lat2")
    Lon2=request.POST.get("Lon2")
    print("astar", Lat1, Lon1, Lat2, Lon2)
    return JsonResponse({'foo':'bar'})    


##################extras#####################################
def index(request):
    return HttpResponse("Hello, world")

def detail(request, id):
    return HttpResponse("You're looking at question %s." % id)

def results(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id)

def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)   

################################################################

     
