# oops is an object oriented programming, it is a way to structure code using :class and object
# a class is a blueprint 
# ex: like a template of a student   like name and marks
# an object is a real instance created from the student
# ex: geetha with 90 marks
# init is a constructor runs automatically when object is created

class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
    def is_expensive(self):
           if self.price>100000:
                print("expensive car")
           else:
                print("affordable car")
c1=Car("BMW",20000000)
c1.display()
c1.is_expensive()



