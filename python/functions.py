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

def reverse_string(s):
    rev=""
    for ch in s:
        rev=ch+rev
    return rev
print(reverse_string("geetha"))
    


