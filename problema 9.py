

n=int(input("Introdu numărul: "))
for p in range(1,n+1): #inclusiv n
    s=0
    for i in range(1,p):
        if p%i==0:
            s+=i
    if s==p:
        print(p,end=",")