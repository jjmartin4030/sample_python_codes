def oddeven(*m):
    a=[]
    b=[]
    for i in m:
        if(i%2==0):
            a.append(i)
        else:
            b.append(i)
    print(a)
    print(b)
n=int(input("Enter the number"))
c=[]
for i in range(0,n):
    elem=int(input())
    c.append(elem)
oddeven(c)
