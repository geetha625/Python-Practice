#def my_function():
#    print("helloo")
#my_function()

#def greet():
#    print("Hello,Python!")
#greet()

#def add(a,b):
#    print(a+b)
#add(a=10,b=20)

#def square(n):
#    return n*n
#print(square(6))

#def cube(n):
#    return n*n*n
#print(cube(3))

#def max_two(a,b):
#    return max(a,b)
#print(max_two(5,1))

#def sum_list(lst):
#    return sum(lst)
#print(sum_list([1,2,3]))

#def positive_negative(a):
#    if a>0:
#        return "positive"
#    elif a<0:
#        return "negative"
#    else:
#        return "zero"
#print(positive_negative(7))
#print(positive_negative(0))
#print(positive_negative(-2))

#def vowels(s):
#    count=0
#    for ch in s:
#     if ch in "aeiouAEIOU":
#        count+=1
#    return(count)
#print(vowels("geetha"))

#def is_vowel(ch):
#    if ch in "aeiouAEIOU":
#        return "vowel"
#    else:
#        return "not vowel"
#print(is_vowel("g"))

#def reverse_string(s):
#    rev=""
#    for ch in s:
#        rev=ch+rev
#    return rev
#print(reverse_string("geetha"))

#def func_name(fname,lname):
#    print(fname + lname)
#func_name("geetha","gandham")

#def palindrome(s):
#    rev=""
#    for ch in s:
#        rev=ch+rev
#    if rev==s:
#            return("true")
#    else:
#            return("false")
#print(palindrome("madam"))

#def vowels_consonants(s):
#    vowels=0
#    consonants=0
#    for ch in s:
#     if ch in "aeiouAEIOU":
#       vowels+=1
#     else:
#       consonants+=1
#    return vowels,consonants
#print(vowels_consonants("geetha"))

#def challenge(s):
#    digits=0
#    alpha=0
#    special_char=0
#    for i in s:
#        if i.isdigit:
#            digits+=1
#        elif i.isalpha:
#            alpha+=1
#        else:
#            special_char+=1
#    return digits,alpha,special_char
#print(challenge("geetha123@#"))

# *args and **kwargs
# we use when we dont know no of parameters to be passed
#args are stored in tuples and they are positional arguments
#kwargs are stored in dictionaries as they are keyword arguments

#create a func that prints all nums using args
#def nums(*args):
#     print(args)
#nums(1,2,3)

#create a func that prints student details using **kwargs
#def student(**kwargs):
#    print(kwargs)
#student(name="geetha",branch="csm",age=20)

#find max num using *args
#def max_nums(*args):
#    print(max(args))
#max_nums(4,2,6)

#output ?  [error]
#def fun(*args):
#    print(args[0])
#fun()

#length ?    [1]
#def fun(*args):
#    print(len(args))
#fun(10)

#sum
#def sum(*args):
#    total=0
#    for i in args:
#        total+=i
#    return total
#print(sum(2,5,3,8))

#max num without max
#def find_max(*args):
#    max_num=args[0]
#    for i in args:
#        if i>max_num :
#         max_num=i
#    return max_num
#print(find_max(3,1,8,5))

#find avg
#def avg(*args):
#    total=0
#    for i in args:
#        total+=i
#    return total/len(args)
#print(avg(16,34,21))

#find min
#def min(*args):
#    min_num=args[0]
#    for i in args:
#        if i<min_num:
#            min_num=i
#    return min_num
#print(min(5,8,1,2))

#scope
# a variable created in the main body is called global variable which belongs to global space
#x=300
#def fun():
#    print(x)
#fun()

#if you assign a same variable inside and outside the function ,python treat them as separate variables and 
# it prints the local variable first and global variable later
#x=300
#def fun():
#    x=20
#    print(x)
#fun()
#print(x)

#if you want to create a global variable but you are stuck in local scope, use global keyword
#def fun():
#    global x
#    x=200
#fun()
#print(x)
#if you want to change the global variable also refer to global keyword

#python decorators
# it add some features to another function 
#def changecase(func):
#    def myinnerfunc():
#        return func().upper()
#    return myinnerfunc()
#@changecase
#def myfunc():
#    return "helloo geethaa"
#print(myfunc)

# a decorator can be called many times ,just put the decorator on any function you want change
#def changecase(func):
#    def myinnerfunc():
#        return func().lower()
#    return myinnerfunc()
#@changecase
#def myfunc():
#    return "HELLO GEETHA"
#@changecase
#def otherfunc():
#    return "I AM A STUDENT"
#print(myfunc)
#print(otherfunc)

#def changecase(func):
#    def wrapper():
#        print("function is starting")
#        func()
#        print("function is ending")
#    return wrapper
#@changecase
#def greet():
#    print("hello python")

#decorator with arguments
#def changecase(func):
#    def innerfunc(name):
#        print("starting")
#        func(name)
#        print("ending")
#    return innerfunc
#@changecase
#def myfunc(name):
#    print("hello",name)
#myfunc("geetha")

#def decorator(func):
#    def wrapper(login):
#        print("login successful")
#        func(login)
#    return wrapper
#@decorator
#def dashboard(login):
#    print(login)
#dashboard("welcome to dashboard")

#def decorator(func):
#    def wrapper(user):
#        print("access granted")
#        func(user)
#        print("session ended")
#    return wrapper
#@decorator
#def profile(user):
#    print(user)
#profile("user profile page")

#def decorator(func):
#    def wrapper(*args,**kwargs):
#        print("access granted")
#        result=func(*args,**kwargs)
#        print("session ended")
#        return result
#    return wrapper
#@decorator
#def profile(*args,**kwargs):
#    print("user profile page")
#profile()

#def decorator(func):
#    def wrapper():
#        print("started")
#        func()
#        print("ended")
#    return wrapper
#@decorator
#def show():
#    print("python rocks")
#show()

#def deco(func):
#    def wrapper():
#        return func()*10
#    return wrapper
#@deco
#def num():
#    return 5
#print(num())



#lambdaa
# a lambda is an anonymous functions(a func without name) 
#it is used for 1 line(short) code but it not faster than nrml functions
#used in datascience and ML
#used with builtin funcs lyk map(),filter(),sorted()
#map() is used to iterate through every item in a LIST
#filter() is used to take selected or required items
#sorted() is used to arrange the elements

#syntax:  lambda args:expression

#add=lambda a:a+5
#print(add(2))

#square=lambda a:a*a
#print(square(5))

#sub=lambda a,b,c:a-b-c
#print(sub(4,1,3))

#evenodd=lambda n: "even" if n%2==0 else "odd"
#print(evenodd(7))

#add=lambda a,b:a*b
#print(add(2,3))

#RECURSION
# a RECURSION is a function calling itself meaning you can loop through the data until it reaches the result 
# if uh write the code wrongly it may never terminate 

#def countdown(n):
#    if n<=0:
#        print("done")
#    else:
#        print(n)
#        countdown(n-1)
#countdown(5)

#every recursion has 2 types: 
# 1) base case : it is a condition to stop a loop
# 2) recursive case : the func calling itself with modified argument

#def factorial(n):
#    if n==1:      #base case
#        return 1
#    else:             #recursive case
#        return n*factorial(n-1)
#print(factorial(5))

# always make sure a recursive case should meet its basecase
# without a bse case a recurisive case leads to infinite loop

#def sum(n):
#    if n==0:
#     return n
#    return n+sum(n-1)
#print(sum(5))

#def fibonacci(n):
#    if n==0 or n==1:
#        return n 
#    return fibonacci(n-1) + fibonacci(n-2)
#print(fibonacci(6))

#recursion is also used to process a list
#def sum_lst(lst):
#    if lst==[]:
#        return 0
#    else:
#        return lst[0]+sum_lst(lst[1:])
#print(sum_lst([1,2,3,4,5]))

#def print_lst(lst):
#    if lst==[]:
#        return
#    print(lst[0])
#    print_lst(lst[1:])
#print_lst([10,20,30])

#def fun(lst):
#    if lst==[]:
#        return 0
#    return lst[-1]+fun(lst[:-1])
#print(fun([1,2,3])

#def reverse_lst(lst):
#    if lst==[]:
#        return 
#    print(lst[-1])
#    reverse_lst(lst[:-1])
#reverse_lst([1,2,3,4,5])

#def mystery(n):
#    if n==0:
#        return 1
#    return n*mystery(n-1)
#print(mystery(4))

#def max_lst(lst):
#    if len(lst)==1:
#        return lst[0]
#    max_rest=max_lst(lst[1:])
#    if lst[0]>max_rest:
#        return lst[0]
#    else:
#        return max_rest
#print(max_lst([3,7,2,9,5]))

# GENERATOR
# a generator function will pause and resume their execution
# a generator is an iterator and gives values one by one using YIELD keyword
# generators are used when 1)large data 2)faster in big prblms 3)infinite sequences and 4) to save memory

#def nums():  
#    yield 1
#    yield 2
#    yield 3
#x=nums()
#print(x)
#print(next(x))
#print(next(x))
#print(next(x))

def fibonacci():
    a,b=0,1
    while True:
        a,b=b,a+b
gen=fibonacci()
for i in range(10):
    print(next(gen))








 













    


    

    


