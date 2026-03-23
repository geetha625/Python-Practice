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

'''class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def info(self):
        print("title:",self.title)
        print("author:",self.author)
b=Book("python basics","geetha")
b.info()'''                                # name:python basics author:geetha

'''class Car:
     def __init__(self,brand):
         self.brand=brand
     def show(self):
         print(self.brand)
c1=Car("Ford")
c1.show() '''  # Ford

# CLASS METHOD

# in a class, we usually write instance methods  ( instance is the object created from a class)
# for class methods, we use @classmethod 
# ex: 
'''@classmethod
def method_name(cls):'''
# @classmethod is a decorator , cls is class

# syntax
'''class Student:
  school="DTS school"
  @classmethod
  def show_school(cls):
   print(cls.school)
Student.show_school() '''     # DTS school

# we use class methods when we want to work with class variables
'''class Student:
    school="XYZ school"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_school(cls,new_name):
        cls.school=new_name
print(Student.school)                  #XYZ school
Student.change_school("ABC school")
print(Student.school)'''            # ABC school
# self :
# - refers to object , used in normal methods
# cls :
# - refers to class , used in class methods

'''class Car:
    wheels=4
    @classmethod
    def show(cls):
        print(cls.wheels)    # cls.wheels access the cls variables wheels
Car.show() '''              # 4

'''class Student:
    school="ABC school"
    def __init__(self,name):
        self.name=name
    @classmethod
    def show_school(cls):
        print(cls.school)
Student.show_school() '''        # ABC school

'''class Bank:
    bank_name="RBC"
    def __init__(self,customer_name):
        self.customer_name=customer_name
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
print(Bank.bank_name)
Bank.change_bank_name("HDFC")           
print(Bank.bank_name)'''              # RBC HDFC

'''class College:
    college_name="MVSR"
    def __init__(self,student_name):
        self.student_name=student_name    # BELONGS TO EACH OBJECT
    @classmethod
    def show_college(cls):
        print(cls.college_name)      # BELONGS TO THE CLASS
College.show_college() '''             # MVSR

# STATIC METHOD -no self,no cls
# it does not use object data or class data
# used for utility logic related to the class

# SYNTAX :
'''class MathOperations:
    @staticmethod
    def add(a,b):
        return a+b
print(MathOperations.add(5,3))'''    # 8

'''class Employee:
    @staticmethod
    def is_adult(age):
        return age>=18
print(Employee.is_adult(20))'''          # True

# DIFFERENCES

# instances method - uses objects data
#def show(self):
# class method - uses class data
#@classmethod
#def change(cls):
# static method - uses neither
#@staticmethod:
#def check(x):

'''class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        f=(c*9/5)+32
        return f
print(Temperature.celsius_to_fahrenheit(25)) '''       # 77

'''class Demo:
    #staticmethod
    def greet():
        print("hello")
print(Demo.greet()) '''         # hello none

# INHERITANCE

# INHERITANCE means one class can use the properties and methods of another class
# it helps to reuse the code
# like parent class - gives features, child class - uses those features
# EXAMPLE : dog, car

# SYNTAX :
'''class parent:
    ....
class child(parent):     # the child class inherits from the parent class
    ....'''

'''class Animal:
    def speak(self):
        print("animal makes sound")      # animal makes sound
class Dog(Animal):
    pass
d=Dog()
d.speak()''' 

'''class Person:
    def greet(self):
        print("hello")
class Student(Person):
    def study(self):
        print("studying")
s=Student()
s.greet()               # hello
s.study() '''              # studying

# CHILD CLASS ADDING ITS OWN METHOD
# a CHILD class can use parent methods and have its own methods

'''class Animal:
    def speak(self):
        print("animal makes sound")
class Dog(Animal):
    def bark(self):
        print("dog barks")
d=Dog()
d.speak()          # inehrited method                               # animal makes sound
d.bark()'''        # its own method                                 # dog barks

'''class Vehicle:
    def start(self):
        print("vehicle started")
class Car(Vehicle):
    def drive(self):
        print("car is driving")
c=Car()
c.start()          # vehicle started
c.drive() '''         # car is driving

# METHOD OVERRIDING
# sometimes the child class changes the behaviour of the parent method
'''class Animal:
    def speak(self):
        print("animal makes sound")
class Dog(Animal):
    def speak(self):
        print("dog barks")
d=Dog()
d.speak() '''       # overrides  # dog barks

#class Shape:
#    def area(self):
#        print("calculating area")
#class Square(Shape):
#    def area(self):
#        print("area of square")
#s=Square()
#s.area()         # area of square

# SUPER() in inheritance

# super() is used to call the PARENT CLASS from the child class
# we need super() bcoz when the child class has its own __init__,the parent __init__ does NOT run AUTOMATICALLY so we super() to call it

# example
#class Person:
#    def __init__(self,name):
#        self.name=name
#class Student(Person):
#    def __init__(self,name,age):
#        self.age=age
#s=Student("geetha",21)
#print(s.name)                # error bc0z name was not assigned

# example with super()
#class Person:
# def __init__(self,name):
#    self.name=name
#class Student(Person):
#  def __init__(self,name,age):
#    super().__init__(name)
#    self.age=age
#s=Student("geetha",20)
#print(s.name)              # geetha
#print(s.age)               # 20

# when to use :
# to reuse parent logic
# especially __init__
# when overriding a method but still want parent behaviour

#class Vehicle:
#    def start(self):
#        print("vehicle started")
#class Car(Vehicle):
#    def start(self):
#        super().start()
#        print("car started")
#c=Car()                            
#c.start()
# OUTPUT :
"vehicle started"
"car started"

# MULTILEVEL INHERITENCE
#class A:
#    def showA(self):
#        print("class A")
#class B(A):
#    pass
#class C(B):
#    pass
#c=C()
#c.showA()         # class A

# MULTIPLE INHERITANCE 
# a class can inherit from more than one parent class
# one child : multiple parents

# example :
#class A:
#    def showA(self):
#        print("class A")
#class B:
#    def showB(self):
#        print("class B")
#class C(A,B):
#    pass
#c=C()
#c.showA()        # class A
#c.showB()        # class B
" c inherited from A ,B "

# NOTE :if both parent classes have same method name then python follows MRO(METHOD RESOLUTION ORDER) means it checks from LEFT to RIGHT ORDER
# example
#class A:
#    def show(self):
#        print("A")
#class B:
#   def show(self):
#        print("B")
#class C(A,B):
#    pass
#c=C()
#c.show()         # A

#class Father:
#    def skills(self):
#        print("gardening")
#class Mother:
#    def skills(self):
#        print("cooking")
#class Child(Father,Mother):
#    pass
#c=Child()
#c.skills()          # gardening

# ENCAPSULATION :
# HIDING DATA and CONTROLLING ACCESS to it

" types in python"
#type        Syntax       Access
#public       name          anywhere
#protected    _name         inside class and child
#private      __name        only inside class

# example :
#class Student:
#    def __init__(self):
#        self.name="geetha"        # public
#        self._age=20              # protected
#        self.__marks=88           # private
#s=Student()
#print(s.name)
#print(s._age)
#print(s._Student__marks)      # to access private
#OUTPUT :
#"geetha"
#20
#88

#class BankAccount:
#    def __init__(self,balance):
#        self.__balance=balance
#    def deposit(self,amount):
#        self.__balance+=amount
#    def show_balance(self):
#        print(self.__balance)
#b=BankAccount(0)
#b.deposit(1000)
#b.show_balance()           # 1000

# POLYMORPHISM 
#    same method name but different behaviour ( METHOD OVERRIDING)

#class Animal:
#    def speak(self):
#        print("animal sound")
#class Dog(Animal):
#    def speak(self):
#        print("dog barks")
#class Cat(Animal):
#    def speaks(self):
#        print("cat meows")
#d=Dog()
#c=Cat()
#d.speak()   # dog barks
#c.speak()    # animal sound

#def add(a,b):
#    return a+b
#print(add(2,3))           # 5
#print("hi","geetha")      # hi geetha

#class Shape:
#    def area(self):
#        pass
#class Circle(Shape):
#    def area(self):
#        print("circle area")
#class Square(Shape):
#    def area(self):
#        print("square area")
#Shapes=[Circle(),Square()]
#for s in Shapes:
#    s.area()
# OUTPUT:
"circle area"
"square area"

'''class Bird:
    def Fly(self):
        print("some birds can fly")
class Sparrow(Bird):
    def Fly(self):
        print("sparrow flies")
class Ostrich(Bird):
    def Fly(self):
        print("ostrich cannot fly")
birds=[Sparrow(),Ostrich()]           # for collection of diff objects
for b in birds:                  # calls same method
    b.Fly()
OUTPUT:
"sparrow flies"
"ostrich cannot fly" '''

# PRACTICE QUES

# 1
class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
s=Student("geetha")
s.display()            # geetha

# 2
class Employee:
    def __init__(self,salary):
        self.salary=salary
    def increase_salary(self,amount):
        self.salary+=amount
    def display(self):
        print(self.salary)
e=Employee(20000)
e.increase_salary(5000)
e.display()               # 25000

# 3
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
r=Rectangle(4,3)
print(r.area())                      # 12
print(r.perimeter())                 # 14

# use return when you want to send a value back
# use print() when you want to display inside the method

# 4 STUDENT RESULT
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_pass(self):
        if self.marks>=40:
            return "pass"
        else:
            return "fail"
s=Student("geetha",75)
print(s.is_pass())                    # pass

# 5 STUDENT GRADE 
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=75:
            return "B"
        elif self.marks>=50:
            return "C"
        else:
            return "fail"
s=Student("geetha",82)
print(s.get_grade())                    # B

# 6 BANK ACCOUNT
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            return "insufficient balance"
        else:
            self.balance-=amount
    def display(self):
        print(self.balance)
b=BankAccount(1000)
b.deposit(500)
b.withdraw(200)
b.display()                      # 1300

# 7 COUNT NO. OF OBJECTS
class Student:
     count=0
     def __init__(self,name):
         self.name=name
         Student.count+=1
     def display(self):
         print(self.name)
     @classmethod                       # when we want to work with cls variables
     def total_students(cls):
         print("total students:",cls.count)
s1=Student("geetha")
s2=Student("avinash")
s3=Student("pavani")
s1.display()
s2.display()
s3.display()  
Student.total_students()                        
# OUTPUT:
'''geetha
avinash
pavani
total students: 3 '''

# 8   UPDATE STUDENT MARKS
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def update_marks(self,new_marks):
        self.marks=new_marks
    def display(self):
        print(self.name)
        print(self.marks)
s1=Student("geetha",82)
s1.display()
s1.update_marks(90)
s1.display()                     # 90

# 9 __str__ METHOD
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return "employee name: "+self.name+"\nsalary: "+str(self.salary)
e1=Employee("geetha",48000)                 # geetha
print(e1)                                   # 48000

# 10 FIND HIGHEST SALARY
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.salary)
e1=Employee("geetha",50000)
e2=Employee("ram",630000)
e3=Employee("anu",75000)    
if e1.salary>e2.salary and e1.salary>e3.salary:
    highest=e1
elif e2.salary>e1.salary and e3.salary>e2.salary:
    highest=e2
else:
    highest=e3
print("highest salary:",highest.name,highest.salary)                  # anu 75000

# 11 CLASS VARIABLE AND AVERAGE CALCULATION
class Student:
    total_marks=0
    count=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_marks+=marks
        Student.count+=1
    @classmethod
    def average_marks(cls):
        avg=cls.total_marks/cls.count
        print("average marks:",avg)
s1=Student("geetha",88)
s2=Student("ram",75)
s3=Student("anu",92)    
Student.average_marks()                        # average marks: 85.0

# 12 INHERITANCE
class Person:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print(self.name)
class Student(Person):
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_marks(self):
        print(self.marks)
s=Student("geetha",88)
s.display_name()           # geetha
s.display_marks()           # 88

# use super()
class Person:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print(self.name)
class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks=marks
    def display_marks(self):
        print(self.marks)
s=Student("geetha",88)
s.display_name()           # geetha
s.display_marks()          # 88

# 13 POLYMORPHISM ( METHOD OVERRIDING)
class Animal:
    def sound(self):
        print("animal makes sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")
a=Animal()
d=Dog()
a.sound()           # animal makes sound
d.sound()           # dog barks

# 14 POLYMORPHISM WITH MULTIPLE CLASSES
class Shape():
    def area(self):
        print("area of shape")
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("area of rectangle:",self.length*self.width)
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("area of circle:",3.14*self.r*self.r)
r=Rectangle(4,3)
c=Circle(2)
r.area()            # 12
c.area()            # 12.56

# 15 ENCAPSULATION ( PRIVATE VARIABLE )
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):                
        self.__balance-=amount     # OR if amount>self.__balance:
                                     #      print("insufficient balance")
                                     #  else:
                                     #      self.balance-=amount
    def display_balance(self):
        print(self.__balance)
b=BankAccount(3000)
b.deposit(2000)
b.withdraw(2500)
b.display_balance()           # 2500

# 16 BANK ACCOUNT WITH TRANSACTION HISTORY
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
        self.transactions=[]
    def deposit(self,amount):
        self.__balance+=amount
        self.transactions.append("deposited "+str(amount))  
    def withdraw(self,amount):
        if amount>self.__balance:
            print("insufficient balance")
        else:
            self.__balance-=amount
            self.transactions.append("withdrew "+str(amount))
    def display_balance(self):
        print(self.__balance)
    def show_transactions(self):
        for t in self.transactions:
            print(t)
b=BankAccount(4000)
b.deposit(2000)
b.withdraw(500)
b.display_balance() 
b.show_transactions()



        









    



    
































