n=int(input("Introdu numărul: "))
s=1
s1=1
nr=0
for i in range(2,n+1):
    s=s*2+i
print("Cand Mihai a împlinit",n,"ani, a primit",s,"dolari") #puntul a
while s1<=100:
    nr+=1
    s1=s1*2+nr
print("Cadoul lui Mihai a fost mai mare de 100$,când a împlinit",nr,"ani") #punctul b
