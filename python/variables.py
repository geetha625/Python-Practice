#simple variables
age=20
name="geetha"
cgpa=8.5
print(age)
print(name)
print(cgpa)
#multiple assignment
a,b,c=10,20,30
print(a,b,c)
#global vs local variable
x=100 #global variable
def demo():
    y=50 #local variable
    print("inside function")
    print("x=",x)
    print("y=",y)
demo()
print("outside function")
print("x=",x)
