def rever(n):
    rev = 0
    while (n != 0):
        num = n % 10
        rev = rev * 10 + num
        n = n // 10
    return rev
n = int(input("Enter the number"))
print(rever(n))

