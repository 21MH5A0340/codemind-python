A,B,C=map(int,input().split())
p=(A+B+C)/2
print("%.2f"%(p*(p-A)*(p-B)*(p-C))**0.5)