n=int(input("Enter the Limit of the list"))
a=[]
b=[]
for i in range(0,n):
    elem=input()
    a.append(elem)
    b.append(elem)
a.sort()
print(a)
f=0
if a==b:
    print("yes")
else:
    print("no")
"""for i in range(0,n):
    if a[i]==b[i]:
        f=f+1
if(f==n):
    print("the list are same")
else:
    print("
    """
    
    
