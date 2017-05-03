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
vi_adjids=[]
vi_adjgraphids=[]
vi_graph=[]
vi_cord_list=[]

def adjlist_generate(r):
    del vi_graph[:]
    del vi_cord_list[:]
    del vi_adjids[:]
    del vi_adjgraphids[:]
    

    for i in range(len(r.nodes_in_box)):
        nd=r.queryNode(r.nodes_in_box[i])
        vi_cord_list.append(nd.lon)
        vi_cord_list.append(nd.lat)
        vi_adjids.append(int(nd.id))

        mi=[]
        temp=[]
        for j in range(len(nd.adjPtr)):
            md=r.queryNode2(nd.adj[j],nd.adjPtr[j])
            mi.append(md.lon)
            mi.append(md.lat)
            temp.append(int(md.id))


        vi_graph.append(mi)
        vi_adjgraphids.append(temp)

def AStar_tocord(r):
    del vi_cord_list[:]
    for i in range(len(r.path) ):
        nd=r.queryNode(r.path[i])
        vi_cord_list.append(nd.lon)
        vi_cord_list.append(nd.lat)        


# r=e.rtree(490811040)
# print(r.root)
# r.boundingBox(77.1780,77.2652,28.5985,28.6424,4)
# print(r.nodes_in_box )

################################################################

#for page initial loading 
@csrf_exempt
def req(request):

    response = {'list': [], 'adjlist': [] }
    r=e.rtree(490811040)
    
    maxLat = 28.9689998626709
    maxLong = 77.73299407958984
    minLat = 28.18301010131836
    minLong = 76.69200134277344

    r.boundingBox(minLong,maxLong,minLat,maxLat,1)
    adjlist_generate(r)


    i=0;
    # module_dir = os.path.dirname(__file__)  # get current directory
    # file_path = os.path.join(module_dir, 'data.txt')
    list1=[]
    # with open(file_path) as fp:
    #     for line in fp:
    #         i+=1
    #         # if(i%300000!=0):#change here for no. of nodes.
    #         #     continue;

    #         words = line.split(" ") 
    #         #loc = {'lat':float(words[0]),  'lon': float(words[1]) }
    #         list1.append(float(words[0]))
    #         list1.append(float(words[1]))

            
    #         if(i==100):#change here for no. of nodes.
    #             break;
    
    #print list1            
    #print(request.POST.get('search_name'))
    #list1 = ['physics', 'chemistry', 1997, 2000];
    print(len(vi_cord_list))
    print(len(vi_graph))
    # print(vi_adjids)
    # print(vi_adjgraphids)
    # count=0
    # for i in xrange(0, len(vi_adjids)-1):
    #     print(vi_adjids[i], vi_adjids[i+1])
    #     i+=1
    #     count=0
    #     for i in xrange(0, len(vi_adjgraphids)-1):

    
    #response['list']=vi_cord_list
    #response['adjlist']=vi_graph

    #JsonResponse(response)
    
    context = {'list': vi_cord_list, 'adjlist': vi_graph, 'vi_adjids':vi_adjids, 'vi_adjgraphids':vi_adjgraphids }
    #context = {'list': vi_cord_list}

    return render(request, 'view1.html', context)

    #return JsonResponse({'foo':'bar'})

################################################################

#for  returning list of prefix
@csrf_exempt
def return_list(request):
    print("request param= ", request.POST.get("search"))
    prefix=request.POST.get("search")
    typeOfReq=int(request.POST.get("type"))

    response = {'way_names': [], 'way_ids': [],'node_names': [], 'node_ids': [],  }
    way_names = []
    way_ids = []
    node_names = []
    node_ids = []


    t=e.trie()
    #w=t.search_trie("Hapur Road")
    st=str(prefix)
    #print ("st=", st);

    if(typeOfReq==1):
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
    Type=request.POST.get("type")
    
    t=e.trie()
    if(Type=="nodes"):
        print("nodes inside")
        response['type']=Type
        n=t.search_trie_node(name)
        if(n.nodeptr >= 0):
            t.node_with_nodeid(n.nodeptr)
            for i in t.lat_list:
                node_list.append(float(i)) 
    
    elif(Type=="ways"):
        print("ways inside")
    
        response['type']=Type
        w=t.search_trie(name)
        #print("w=",w.getid())
        #print("w=",w.wayptr)
        if(w.wayptr >= 0):
            t.node_with_wayid(w.wayptr)
            for i in t.lat_list:
                #print (i)
                way_list.append(float(i))
            for i in t.delimiter_list:
                #print (i)
                dlist.append(float(i))
        
    
    # print("lat=", t.lat_list, "\ndlist=", t.delimiter_list)
    # print("nodelist", node_list)

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
    
    admin_level=int(request.POST.get("admin_level"))
    minLat=float(request.POST.get("minLat"))
    minLong=float(request.POST.get("minLon"))
    maxLat=float(request.POST.get("maxLat"))
    maxLong=float(request.POST.get("maxLon"))
    
    

    print("rtree",admin_level, minLat, minLong,maxLat, maxLong)
    
    response = {'list': [], 'adjlist': [] }
    r=e.rtree(490811040)
    r.boundingBox(minLong,maxLong,minLat,maxLat,admin_level)
    adjlist_generate(r)


    # print(len(vi_cord_list))
    # print(len(vi_graph))
    response['list']=vi_cord_list
    response['adjlist']=vi_graph

    r.close()
    #JsonResponse(response)
    #context = {'list': vi_cord_list, 'adjlist': vi_graph}
    #context = {'list': vi_cord_list}

    #return render(request, 'view1.html', context)
    return JsonResponse(response)


################################################################

# def nearestNode(Lat, Lon):
#     response = {'id': -1}

#     # Lat=float(request.POST.get("Lat"))
#     # Lon=float(request.POST.get("Lon"))
#     # print("nearestNode", Lat, Lon)
#     nearestId=r.nearestNode2( Lon,Lat)
#     print("nearestId", nearestId)
#     response['id']=nearestId
#     //return JsonResponse(response)
    
    

################################################################

#for returning shortest path. 
@csrf_exempt
def astar(request):
    r=e.rtree(490811040)
    response = {'list':[]}


    typeOfAstar=int(request.POST.get("type"))

    if(typeOfAstar==1): #point pick on map
        Lat1=float(request.POST.get("Lat1"))
        Lon1=float(request.POST.get("Lon1"))
        Lat2=float(request.POST.get("Lat2"))
        Lon2=float(request.POST.get("Lon2"))
        nearestId1=r.nearestNode2( Lon1,Lat1)
        nearestId2=r.nearestNode2( Lon2,Lat2)
    
        print("astar", Lat1, Lon1, Lat2, Lon2, "near", nearestId1,nearestId2 )
        
        
        
        r.AStar(nearestId1,nearestId2)
        AStar_tocord(r)
        response['list']=vi_cord_list
        print("vi_cord_list=", vi_cord_list)

        r.close()
        return JsonResponse(response)
    
    elif(typeOfAstar==2):  #by name search 
        srcId=long(float(request.POST.get("srcId")))
        dstId=long(float(request.POST.get("dstId")))
        print("astar, type2", srcId, dstId)
        
        r.AStar(srcId,dstId)
        AStar_tocord(r)
        response['list']=vi_cord_list
        print("vi_cord_list=", vi_cord_list)


        r.close()
        return JsonResponse(response)   


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

     
