n=int(input("Enter the number of list elements"))
a=[]
print("Enter the elements")
for i in range(0,n):
    ele=input()
    a.append(ele)
for i in a:
    d=a.count(i)
    print("the count",i,"is",d)
