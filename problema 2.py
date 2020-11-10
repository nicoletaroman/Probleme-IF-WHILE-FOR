import math

n=int(input('Dati un nr mai mare ca 0 '))
s=0
for i in range (1,n+1):
    s+=(math.factorial(i))

print ('Suma 1!+2!+...+n!= ',s)



