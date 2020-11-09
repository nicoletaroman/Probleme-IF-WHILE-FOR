#punctul a
n=int(input("dati un nr"))
s1=0
p=0
for i in range(1,n+1):
    s1+=i**3
    p+=i
    s2=p**2
   
if s1==s2:
    print("sunt egale")
if s1>s2:
    print("s1 este mai mare")
if s2>s1:
    print("s2 este mai mare")

#punctul b 
nb=int(input("dati un nr"))
m=0
l=0
for nr in range(1,nb+1):
    l+=nr**2
    s1b=3*l
    m+=nr
    s2b=nb**3+nb**2+m
if s1b==s2b:
    print("sunt egale")
if s1b>s2b:
    print("prima suma e mai mare")
if s1b<s2b:
    print("a doua suma e mai mare")


