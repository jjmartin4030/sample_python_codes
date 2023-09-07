n=int(input("Enter the number"))
a=[]
b=[]
print("Enter the elements")
for i in range(0,n):
    elem=int(input())
    a.append(elem)
print("Enter the 2nd elements")
for i in range(0,n):
    elem=int(input())
    b.append(elem)
a.extend(b)
b.clear()
for i in a:
    if i%2==0:
        a.append(i)
    else:
        a.remove(i)
        b.append(i)

print(a)
print(b)

