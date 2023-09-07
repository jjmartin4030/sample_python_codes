def simple(p,n,r):
    si=p*n*r
    return si
p=int(input("Enter the principle amount"))
n=int(input("Enter the year"))
r=int(input("Enter the rate of intrest"))
print("The simple intrest",simple(p,n,r))
