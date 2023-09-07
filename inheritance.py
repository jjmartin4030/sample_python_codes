""""Single inheritance
class School:
    def open(self):
        print("school class")
class College(School):
    def start(self):
        print("college open")
obj=College()
obj.open()
obj.start()
"""
"""
class School:
    def open(self):
        print("school class")
class Class1(School):
    def start(self):
        print("college open")
class Student(Class1):
    def present(self):
        print("The student is present")
obj=Student()
obj.open()
obj.start()
obj.present()
"""
class Calculator1:
    def add(self,a,b):
        sum=a+b
        print(sum)
class Calculator2:
    def sub(self,a,b):
        sub=a-b
        print(sub)
class Calculator3:
    def multi(self,a,b):
        multi=a*b
        print(multi)
class Calculator(Calculator1,Calculator2,Calculator3):
    def div(self,a,b):
        div=a/b
        print(div)
obj=Calculator()
a=int(input("Enter the number "))
b=int(input("Enter the number"))
obj.add(a,b)
obj.sub(a,b)
obj.multi(a,b)
obj.div(a,b)