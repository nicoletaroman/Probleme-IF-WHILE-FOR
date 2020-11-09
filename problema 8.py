n1=int(input("dati un nr"))
n2=int(input("dati un nr"))
n3=int(input("dati un nr"))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    if n1==n2==n3:
        print("echilateral")
    if n1!=n2!=n3:
        print("scalen")
    if (n1==n2 and n1!=n3) or (n2==n3 and n1!=n2) or (n1==n3 and n1!=n2):
        print("isoscel")
else:
  print("nu este triunghi")