p,r,t=map(int,input().split())
k=(1+(r/100))
h=k**t
print("%.2f"%(p*h))