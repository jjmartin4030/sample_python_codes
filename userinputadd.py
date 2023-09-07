n=int(input("Enter the number to be inserted"))
a=[]
print("Enter the elements")
for i in range(0,n):
    ele=int(input())
    a.append(ele)
print("The Elements are",a)
b=[]
print("Enter the numbers ")
for i in range(0,n):
    elem=int(input())
    b.append(elem)
print("The Elements are")
print(b)
c=[]
for k in range(0,n):
    c.append(a[k] + b[k])
print("Sum is",c)
d=[]
f=[]
for j in c:
    if(j%2==0):
        d.append(j)
    else:
        f.append(j)
        
print("The Odd list are",f)
print("The even list are",d)
