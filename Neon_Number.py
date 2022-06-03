n=int(input())
sq=n*n
c=0
while sq>0:
    r=sq%10
    c=c+r
    sq=sq//10
if c==n :
    print("Neon Number")
else:
    print('Not Neon Number')