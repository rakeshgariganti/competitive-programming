tc=int(raw_input())
days=[31,28,31,30,31,30,31,31,30,31,30,31]
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
def leapyr(n):
    if n % 4 != 0:
        return False
    elif n % 100 != 0:
        return True
    elif n % 400 != 0:
        return False
    else:
        return True
while tc>0:
	tc-=1
	d,m,y=raw_input().split()
	d=int(d)
	y=int(y)
	d=d-1
	if d==0:
		curindex=months.index(m)
		m=months[(curindex-1)%12]
		d=days[(curindex-1)%12]
		if m=="December":
			y=y-1
		if m=="February":
			if leapyr(y):
				d+=1
	print d,m,y