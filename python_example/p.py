import example as e

vi_graph=[]
vi_cord_list=[]
def adjlist_generate(r):

	for i in xrange(0, len(r.nodes_in_box)):
		nd=r.queryNode(r.nodes_in_box[i])
		vi_cord_list.append(nd.lon)
		vi_cord_list.append(nd.lat)
		mi=[]
		for j in range(len(nd.adjPtr)):
			md=r.queryNode2(nd.adj[j],nd.adjPtr[j])
			mi.append(md.lon)
			mi.append(md.lat)
		vi_graph.append(mi)


t=e.trie()
w=t.search_trie("Hapur Road")
print(w.wayptr)
st="A"
t.display_prefix(st,len(st),0)
li=w.getptr()
print(li)
t.node_with_wayid(w.wayptr)
print(t.prefix)

t.display_prefix_node("Mo",2,0)
print(t.prefix)


r=e.rtree(490811040)
print(r.root)
r.boundingBox(77.1780,77.2652,28.5985,28.6424,4)
print(r.nodes_in_box )

#for i in r.adjlist:
#	print(i)

adjlist_generate(r)
print(vi_graph)
print(vi_cord_list)

r.close()
