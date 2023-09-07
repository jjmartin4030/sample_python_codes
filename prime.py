def prime(n):
    flag=0
    for i in range(1,n+1):
        if(n%i==0):
            flag=flag+1
    return flag
n=int(input("Enter the number"))
flag=prime(n)
if(flag==2):
    print("The Number",n,"is a prime number")
else:
    print("Not prime number")
