a=["😀","😀","😀"]
b=["😀","😀","😀"]
c=["😀","😀","😀"]
ma=[a,b,c]
x=input("enter num")
f=int(x[0])
l=int(x[1])
ma[l-1][f-1]="x"#last digit of x represents the row value of ma
for i in ma:
    print(i)
