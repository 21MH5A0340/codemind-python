t=int(input ())
c=0
while (t!=0 or c>=10):
	if t==0:
		t=c
		c=0
	c+=t%10
	t=t//10
print(c)