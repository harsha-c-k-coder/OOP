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

#program 4:
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name:{self.name}\nSalary:{self.salary}")
e1=employee("harsha",20000)
e1.display()

#program 3:
class bankaccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
        
    def deposit(self):
        deposit_amount=int(input("enter deposit amount:"))
        self.balance+=deposit_amount
    def withdraw(self):
        amount=int(input("enter the withdraw amount:"))
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("insufficient balance")
    def display(self):
        print("Account holder:",self.account_holder)
        print("Account number:",self.account_number)
        print("balance:",self.balance)
a=bankaccount("harsha",1234,1000)
a.deposit()
a.withdraw()
a.display()

#program 5:
class library:
    def __init__(self,library_name,location,total_books):
        self.library_name=library_name
        self.location=location
        self.total_books= total_books
    def add(self):
        n=int(input("enter the number of books to return back:"))
        self.total_books+=n
    def remove(self):
        n=int(input("number books going out:"))
        self.total_books-=n
    def display(self):
        print("Library name:",self.library_name)
        print("Location:",self.location)
        print("Total number of books:",self.total_books)
b=library("central library","banglore",20)
b.add()
b.remove()
b.display()



