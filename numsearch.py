n=int(input("Enter the number of list elements"))
a=[]
flag=0
print("Enter the elements")
for i in range(0,n):
    ele=input()
    a.append(ele)
b=input("Enter the number to be searched")
for i in range(0,n):
    if(a[i]==b):
        print(b,"is found at pos",i)
        break
else:
    flag=1
if(flag==1):
    print("not found")
