re=input("")
de=input("")
dv=input("")
s=""
ch=0
le=""
for i in re:
    if i!= de:
        #print(i,re.index(i))
        s=s+i
        #print(s)
        le=s[-1]
        #print("last ele fir c =",le)
    if i==de and i != le:
        s=s+i
        #print(i, re.index(i))
        #print(s)
        le=s[-1]
        #print("last ele sec c =",le)
    elif i ==de and i==le:
        #print(i, re.index(i))
        s=s+dv
        le = s[-1]
        #print(s)
        #print("last element of floop",le)
        ch+=1
print(s)
print(ch)
