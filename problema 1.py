
i=int(input("dati nr de zile"))
if i in (28,29,30,31):
    if ((i==28)or (i==29)):
        print("februarie")
    if (i==30):
        print("aprilie,iunie,septembrie,noiembrie")
    if (i==31):
        print("ianuarie,martie,mai,iulie,august,octombrie,decembrie")
else:
    print("nr de zile nu e corect")