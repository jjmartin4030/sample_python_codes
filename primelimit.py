def prime(n):
    for i in range(1,n):
        flag=0
        for j in range(1,i+1):
            if(i%j==0):
                flag=flag+1
        if(flag==2):
            print(i)
n=int(input("Enter the number"))
prime(n)
"""if(flag==2):
    print("The Number",n,"is a prime number")
else:
    print("Not prime number")
"""
