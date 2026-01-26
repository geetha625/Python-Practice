#len of string

#a="hello, world!"
#print(len(a))

#checking string

#txt="the best things in life are free!"
#print("free" in txt)

#txt="the best things in life are free!"
#if "free" in txt:
 #   print("yes, 'free' is present.")

#txt="hello world"
#if "hello" not in txt:
 #   print("no, 'hello' is not present.")
#else:
   # print("yes, 'hello' is present.")

#slicing strings

#b="hello, world!"
#print(b[2:5])

#b="hello, world!"
#print(b[:5])

#b="hello, world!"
#print(b[2:])

#b="hello, world!"
#print(b[-5:-2])

#modifying strings

#b="hello, world!"
#print(b.upper())

#b="Hello, World"
#print(b.lower())

#remove whitespace
#a=" hello, world! "
#print(a.strip())

#replace string
#a="hello, world!"
#print(a.replace("h",'j'))

#a="hie, geetha"
#print(a.replace('hie','hello'))

#a='hie, geetha' 
#replace=a.replace('hie','hello').replace('geetha','durga')
#print(replace)

#split string
#a="hello, world!"
#print(a.split(",")) #split() returns in lists not in string whenever it sees a , it separates 

#str concatenation
#a="hello"
#b="world"
#c=a+" "+b
#print(c)   #to combie a,b with space in between in variable c

#f-strings
#txt=f"welcome to the world of {5+5}"
#print(txt)

#age=19
#txt=f"my name is geetha,i am {age}"
#print(txt)

#txt="geetha"
#for i in txt:
 #   x=txt.count(i)
#print(x)
 
#txt="geetha"
#print(txt[0]+txt[:0:-1])  #reversing a string

#print("python">"java")  #comparing strings
#print("apple"<"banana")  #comparing strings

#print("hello"=="Hello")  #comparing strings
#print(not(False or True))

#1.reverse a string without using built-in funcs
#a="geetha"
#print(a[::-1])

#2.revere the string keeping the first char same
#a="geetha"
#print(a[0]+a[:-6:-1])

#3.reverse the string keeping the last char same
#a="geetha"
#print(a[-1]+a[-2::-1])

#4.reverse only words in a sentence,not the sentence itself
#a="hello world"
#print(a[-7::-1]+" "+a[-1:-7:-1])

#5.reverse a string except special chars
#a="g@ee#tha"
#print(a[-1]+a[-7]+a[-2:-4:-1]+a[-4]+a[-5:-7:-1]+a[-8])

#palindrome
#6.check whether a string is a palindrome
#a="wow"
#if a==a[::-1]:
#    print("palindrome")
#else:
 #   print("not a palindrome")

#7.check whether a string is a palindrome or not without using slicing
#a="madam"
#rev=""
#for i in a:
 #   rev=i+rev
#if a==rev:
 #   print("palindrome")
#else:
  #  print("not a palindrome")

#8.check palindrome ignoring case
#a="Madam"
#if a.upper()==a[::-1].upper():
 #   print("palindrome")

#9.check palindrome ignoring spaces 
#a="nurses run"
#a=a.replace(" ","")
#if a==a[::-1]:
 #   print("palindrome")

    









