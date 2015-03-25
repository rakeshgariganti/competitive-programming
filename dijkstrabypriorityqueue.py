from pythonds import PriorityQueue

dij(graph,start):
	pq=PriorityQueue()
	distances={}
	distances[start]=0
	pq.buildHeap([(graph[i][j],j) for i in graph:for j in i])
