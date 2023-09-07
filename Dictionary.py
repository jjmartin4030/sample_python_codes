a={
     "name":"Joseph",
     "age":21,
     "address":"Maliyekkal house ,chalakudy",
     "phone no.":123456789,
     "salary":30000.40,
     "friends":["joyal","john",],
     "mm":False
    }
a["gender"]="male"
a["salary"]=40000.45
"""
print(a)
l=len(a)
print(l)
b=dict(name="John",age=21)
print(b)
x=a["name"]
print(x)
print(a.get("name"))
print(a.keys())
print(a.values())
print(a.items())

if "name" in a:
    print("Key is present in this dictionary")
"""
a.pop("name")
a.popitem()
for i,j in a.items():
    print(i,":",j)
