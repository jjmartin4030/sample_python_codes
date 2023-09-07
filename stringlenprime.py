n=input("Enter the String")
l=len(n)
print(l)
a=[]
f=0
for i in range(1,l+1):
    if(l%i==0):
        f=f+1
if(f==2):
    a.append(l)
    print(a)
