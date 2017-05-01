import example as e
t=e.trie()
w=t.search_trie("Hapur Road")
print(w.wayptr)
st="A"
t.display_prefix(st,len(st),0)
li=w.getptr()
print(li)
t.node_with_wayid(w.wayptr)
print(w.getlevel())
print(t.lat_list)
print(t.prefix)

n=t.search_trie_node("Modinagar")
t.node_with_nodeid(n.nodeptr)
print(t.lat_list)

t.close()
"""
r=e.rtree(89816,"test.txt")
r.boundingBox(77.1780,77.2652,28.5985,28.6424,1)
for i in r.nodes_in_box:
	print(i)
"""
