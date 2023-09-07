n=int(input("Enter the number of list elements"))
a=[]
flag=0
print("Enter the elements")
for i in range(0,n):
    ele=input()
    a.append(ele)
a.sort()
b=[]
print("Enter the elements")
for i in range(0,n):
    ele=input()
    b.append(ele)
b.sort()
for i in a:
    for j in b:
        if i==j:
            flag=1
        else:
            flag=0
if (flag==1):
    print("The list is symmetric")
else:
    print("The list is not symmetric")
