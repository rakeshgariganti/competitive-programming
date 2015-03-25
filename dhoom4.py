from collections import deque
mapper=map
makeint=int
rawinput=raw_input
own,lock=mapper(makeint, rawinput().split(" "))
n=input()
others=mapper(makeint, rawinput().split(" "))
keys=[-1]*100000
keys[own]=0
q=deque()
q.append(own)
while len(q)>0:
	current=q.popleft()
	if current==lock:
		break
	for i in others:
		to=(current*i)%100000
		if keys[to]==-1:
			keys[to]=keys[current]+1
			q.append(to)
print keys[lock]

