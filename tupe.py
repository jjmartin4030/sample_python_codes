a=("joseph",860)
p=type(a)
print(p)
b=len(a)
print(b)
print(a)
for i in a:
    print(i)
c=("john","martin")
d=a+c
print(d)
print(d[0:3])
f=a,c,d
print(f)
g=list(a)
g.pop()
print(g)
g.append("a")
print(g)
a=tuple(g)
print(a)
if "joseph" in a:
    print("yes")
