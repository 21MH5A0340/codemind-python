t=int(input())
for c in range(t+1):
	k=0
	for i in range(1,c):
		if t%i==0:
			k=k+i
if t==k:
	print("True")
else:
		print("False")