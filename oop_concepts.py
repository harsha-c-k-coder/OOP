#program 1:
class student:
    def __init__(self,age,name):
        self.age=age
        self.name=name
s1=student(19,"harsha")
print(s1.age)
print(s1.name)

#program 2:
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
c1=car("Mercedes-Benz","C-Class")
print(c1.brand)
print(c1.model)

#program 3:
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("area:",self.length*self.width)
    def perimeter(self):
        print("perimeter:",2*(self.length+self.width))
r=rectangle(2,3)
r.area()
r.perimeter()
