# oops is an object oriented programming, it is a way to structure code using :class and object
# a CLASS is a blueprint used to create objects, it defines the properties and behaviours(methods)
# ex: like a template of a student   like name and marks
# an OBJECT is an instance of a class , it represents a real world entity and contains the data and functions defined in the class
# ex: geetha with 90 marks
# init is a constructor runs automatically when object is created
# self represents the current instance of the class and allows to access object attributes and methods

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
t2=Test()'''   # every time we create an object, the init method runs automatically

'''class Demo:
    def __init__(self):
        x=10
d=Demo()
print(d.x)'''   # attribute error 

'''class Test:
    def __init__(self):
        self.x=5
t1=Test()
t2=Test()
t1.x=20
print(t1.x)
print(t2.x)'''   # 20 5

class Test:
    x=10
t1=Test()
t2=Test()
t1.x=20
print(t1.x)
print(t2.x)
print(Test.x)













