m=int(input("dati un nr"))
n=int(input("dati un nr"))
p=0
if m<n:
     while m**p<=n:
        p+=1
        if m**p==n:
            print("este puterea",p)
        
else:
    print("primul nr trebuie sa fie mai mic")
