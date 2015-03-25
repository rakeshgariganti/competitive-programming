import string
while True:
	try:
		s=raw_input()
		s=s.split("//")
		c=string.replace(s[0],"->",".")
		if len(s)>1:
			print c+"//"+"//".join(s[1:])
		else:
			print c
	except Exception, e:
		exit(0)