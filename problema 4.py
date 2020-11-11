n=int(input("dati numaratorul"))
m=int(input("dati numitorul"))
p=int(input("dati numaratorul"))
l=int(input("dati numitorul"))
from fractions import Fraction
print("suma este =",Fraction(n,m)+Fraction(p,l))
print("produsul este =",Fraction(n,m)*Fraction(p,l))