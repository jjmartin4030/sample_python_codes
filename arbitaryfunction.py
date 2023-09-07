def fun(*m):
    res = 0
    for i in m:
        res = res + i
    return res
res=fun(1, 2, 3)
print(res)