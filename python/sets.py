#write a program to print all elements of a set using a loop
#x={1,2,3}
#for i in x:
#    print(i)

#check whether an element exists in a set
#x={1,2,3,4,5}
#if 3 in x:
#    print("yes")
#else:
#    print("no")

#check output
#s={10,20,30}
#print(40 in s)

#write a program to add one element to a set
#s={10,20,30,40}
#s.add(50)
#print(s)

#add multiple elements
#s={10,20,30,40}
#t={"a","b","c"}
#s.update(t)
#print(s)

#check output
#s={1,2,3}
#s.add(2)
#print(s)

#s={"apple","banana","cherry"}
#s.remove("banana")
#print(s)

#s={"apple","banana","cherry"}
#s.remove(2)
#print(s)     #raise an error

#s={1,2,3}
#s.discard(2)
#print(s)

#s={1,2,3}
#s.discard(5)
#print(s)   #will not raise an error

#s={"apple","banana","cherry"}
#s.pop()
#print(s)

#s={1,2,3,4,5}
#s.clear()
#print(s)

#s={1,2,3,4}
#del s
#print(s)

#s={1,2,3,4,5}
#for x in s:
#   print(s)

#remove vs discard
#s={10,20,30,40}
#s.remove(20)
#s.discard(50)
#print(s)

#pop in set
#s={1,2,3,4}
#s.pop()
#print(s)

#clear vs del
#s={5,6,7}
#s.clear()
#print(s)

#s={5,6,7}
#del s
#print(s)

#check
#s={10,20,30,40}
#if 50 in s:
#    print("yes")
#else:
#    print("no")


#set1={"a","b","c"}
#set2={1,2,3}
#set3=set1.union(set2)
#print(set3)

#set1={"a","b","c"}
#set2={1,2,3}
#set3=set2|set1
#print(set3)

#set1={"a","b","c"}
#set2={1,2,3}
#set3={"john","alena"}
#set4=set1.union(set2,set3)
#print(set4)

#set1={"a","b","c"}
#set2={1,2,3}
#set1.update(set2)
#print(set1)

#x={1,2,3}
#y=(5,6,7)
#z=x.union(y)
#print(z)

#set1={"apple",1,"banana",0}
#set2={True,"google",1,"apple",2}
#set1.intersection_update(set2)
#print(set1)

#join sets

#1.join 2 sets using union
#a={1,2,3}
#b={3,4,5}
#c=a.union(b)
#print(c)

#2.using update
#a={10,20}
#b={20,30,40}
#a.update(b)
#print(a)

#3.using intersection
#s1={1,2,3,4}
#s2={3,4,5,6}
#s3=s1.intersection(s2)
#print(s3)

#4.find elements in only 1st set
#a={1,2,3,4}
#b={3,4,5}
#c=a.difference(b)
#print(c)

#5.find elemnts not common in both sets
#x={1,2,3}
#y={3,4,5}
#z=x.symmetric_difference(y)
#print(z)

#6.merge multiple sets
#s1={1,2}
#s2={3,4}
#s3={4,5}
#s4=s1|s2|s3
#print(s4)

#7.check if 2 sets are equal
#a={1,2,3}
#b={3,2,1}
#if a==b:
#    print("true")
#else:
 #   print("false")

#8.check if a is subset of b
#a={1,2}
#b={1,2,3,4}
#if a.issubset(b):
#    print("true")
#else:
#    print("false")

#9.remove common elemnts from both sets
#a={1,2,3,4}
#b={3,4,5}
#a.difference_update(b)
#print(a)
#print(b)

#10.find unique elements
#l1=[1,2,3,4,4,5]
#l2=[3,4,6,7]
#s=set(l1).union(set(l2))
#print(s)

''' SETS ARE USED TO STORE MULTIPLE VALUES IN A SINGLE VARIABLE
 IT IS WRITTEN IN { } 
 IT DOESNT ALLOW DUPLICATES
  IT DOESNT FOLLOW ANY ORDER '''

''' SET METHODS '''
fruits={"apple","mango","banana"}

# add() method , random
fruits.add("orange")
print(fruits)                       # {'apple', 'banana', 'orange', 'mango'} 

# pop() method , random
fruits.pop()
print(fruits)                       # {'banana', 'orange', 'mango'} , random

# remove () method ,specified
fruits.remove("banana")
print(fruits)                       # {'mango', 'orange'}

x={"geetha","swetha","swathi"}
y={"microsoft","google","swathi"}

# difference() method
print(y.difference(x))     # {'microsoft', 'google'}
print(x.difference(y))        # {'swetha', 'geetha'}

# intersection() method
print(x.intersection(y))     # {'swathi'}

# union() method
print(x.union(y))              # {'swetha', 'microsoft', 'geetha', 'swathi', 'google'}

# update() method
x.update(y)
print(x)              # {'google', 'swetha', 'microsoft', 'swathi', 'geetha'}

