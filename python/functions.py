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
def fun():
    global x
    x=200
fun()
print(x)



    


    

    


