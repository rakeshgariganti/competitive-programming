graph = {'s': {'a': 2, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}}
visited=[]
distances={}
preds={}
def dijkstra(src,dest):
	if src not in graph:
		exit()
	if dest not in graph:
		exit()
	if src==dest:
		path=[]
		pred=dest
		while pred!=None:
			path.append(pred)
			pred=preds.get(pred,None)
		print distances[dest]
	else:
		if not visited:
			distances[src]=0
		for i in graph[src]:
			if i not in visited:
				newdist=distances[src]+graph[src][i]
				if newdist<distances.get(i,float('inf')):
					distances[i]=newdist
					preds[i]=src
		visited.append(src)
		nvisited={}
		for i in graph:
			if i not in visited:
				nvisited[i]=distances.get(i,float('inf'))
		x=min(nvisited,key=nvisited.get)
		dijkstra(x, dest)
dijkstra('s', 't')