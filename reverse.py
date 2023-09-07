n=int(input("Enter the number"))
a=[]
print("Enter the elements")
for i in range(1,n+1):
    elem=input()
    a.append(elem)
b=[]
for j in range(n-1,-1,-1):
    d=0
    d=a[j]
    b.append(d)
print("The reverse of the list are")
for i in b:
    print(i)
