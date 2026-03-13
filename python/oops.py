# oops is an object oriented programming, it is a way to structure code using :class and object
# a CLASS is a blueprint used to create objects, it defines the properties and behaviours(methods)
# ex: like a template of a student   like name and marks
# an OBJECT is an instance of a class , it represents a real world entity and contains the data and functions defined in the class
# ex: geetha with 90 marks
# init is a constructor runs automatically when object is created
# SELF represents the current instance of the class and allows to access object attributes and methods

#class Car:
#    def __init__(self,brand,price):
#        self.brand=brand
#        self.price=price
#    def display(self):
#        print("brand:",self.brand)
#        print("price:",self.price)
#    def is_expensive(self):
#           if self.price>100000:
#                print("expensive car")
#           else:
#                print("affordable car")
#c1=Car("BMW",20000000)
#c1.display()
#c1.is_expensive()

'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("hello, my name is "+ self.name)
p1=Person("geetha",20)
p1.greet() '''

# we use init to assign initial values to object properties , it automatically runs
# default init value
'''class Person:
    def __init__(self,name,age=20):
        self.name=name
        self.age=age
p1=Person("geetha")
p2=Person("pavani",21)
print(p1.name,p1.age)
print(p2.name,p2.age)'''

# init can have multiple parameters
'''class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
p1=Person("geetha",20,"hyderabad")
print(p1.name,p1.age,p1.city)'''

'''class Test:
    def __init__(self):
        print("object created")
t1=Test()
t2=Test()   # every time we create an object, the init method runs automatically'''

'''class Demo:
    def __init__(self):
        x=10
d=Demo()
print(d.x)'''  # attribute error 

'''class Test:
    def __init__(self):
        self.x=5
t1=Test()
t2=Test()
t1.x=20
print(t1.x)
print(t2.x) '''  # 20 5

'''class Test:
    x=10
t1=Test()
t2=Test()
t1.x=20
print(t1.x)
print(t2.x)
print(Test.x) '''  # 20 10 10

'''class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
acc=BankAccount("geetha",1000)
acc.deposit(500)
print(acc.balance)'''    #1500

'''class Demo:
    def __init__(self):
        self.x=10
    def change(self):
        self.x=20
d=Demo()
d.change()
print(d.x)'''   # 20

'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
e1=Employee("geetha",50000)   
e1.display()'''              # name:geetha   salary:50000

#class Test:
#   def __init__(self):
#       self.a=5
#   def show(self):
#       print(self.a)
#t=Test()
#t.show()       #5

'''class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def multiply(self):
        return self.a*self.b
c=Calculator(5,3)
print(c.add())
print(c.multiply())'''   # 8 15 

# or

'''class Calculator:
    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b
c=Calculator()
print(c.add(5,3))
print(c.multiply(5,3))'''

'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
       if self.marks>=90:
          return "A"
       elif self.marks>=75:
          return "B"
       elif self.marks>=50:
          return "C"
       else:
          return "fail"
s=Student("geetha",82)
print(s.grade()) '''            # B

'''class Counter:
    def __init__(self):
        self.startvalue=0
    def increment(self):
        self.startvalue=+1
    def decrement(self):
        self.starvalue=-1
c=Counter()
c.increment()
c.decrement()
print(c.startvalue)'''      #1

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def info(self):
        print("title:",self.title)
        print("author:",self.author)
b=Book("python basics","geetha")
b.info()




















