# operators
x=3
y=2
print(x+y)  #addition
print(x-y)  #subtraction
print(x*y)  #multiplication
print(x/y)  #division
print(x%y)  #modulus
print(x**y) #exponentiation
print(x//y) #floor division

# comparision operators           ( used to assign values to variables)
x=5
y=3
print(x==y)  #equalto
print(x!=y)  #not equal to
print(x>y)   #greater than
print(x<y)   #less than
print(x>=y)  #greater than or equal to
print(x<=y)  #less than or equal to

# assignment operators  (must be on their own line not inside print())
x,y=5,8
x=y
print(x)  # 8
x+=y           # x=x+y
print(x)  # 16
x-=y           # x=x-y
print(x)  # 8
x*=y           # x=x*y
print(x)  # 64
x%=y          
print(x)   # 0

# logical operators        ( used to combine conditional statements)
x=5
y=8
print(x>y and x!=y)
print(x and y)
print(x or y)
print(not y)

# membership operators    ( used to check the sequence in objects)
x=[1,2,3,4,5]
y=4
print(y in x)
print(y not in x)

