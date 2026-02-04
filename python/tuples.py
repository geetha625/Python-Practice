#create a tuple with values 10,20,30,40 and print it
#thistuple=(10,20,30,40)
#print(thistuple)

#create a tuple with 1 element 50 and print its type
#thistuple=(50)
#print(type(thistuple))

#create a tuple containing int,float,string,boolean
#thistuple=(10,2.5,"geetha",True)
#print(thistuple)

#access tuples
#t=(5,10,15,20,25)
#print(t[0],t[-1],t[2])

#t=("a","b","c","d")
#print(t[-2])

#t=(1,2,3,4)
#print(t[0:])

#use loop
#t=(1,2,3,4,5)
#for x in t:
#    print(x)

#print all elements using for loop with index
#t=(1,2,3,4,5)
#for x in range(len(t)):
#    print(x)

#use while loop
#t=(1,2,3,4,5)
#i=0
#while i<len(t):
#    print(t[i])
#    i=i+1

#print only even nums
#t=(3,7,2,9,5)


#count nums greater then 10
#t=(5,12,18,7,20)
#count=0
#for i in t:
#    if i>10:
#        count+=1
#print(count)

#tuple object does not support item assignment
#t=(1,2,3)
#t[1]=5
#print(t)

#write code to add 5 to the list inside the tuple
#t=(1,[2,3],4)
#t[1].append(5)
#print(t)

#print the sum of all elements in a tuple
#t=(10,20,30)
#total=0
#for i in t:
#    total+=i
#print(total)

#x=("apple","banana","cherry")
#y=list(x)
#y[1]="kiwi"
#x=tuple(y)
#print(x)

#x=("apple","banana","cherry")
#y=list(x)
#y.append("orange")
#x=tuple(y)
#print(x)   

#x=(1,2,3,4) 
#y=(5,)
#x+=y
#print(x)

#x=(1,2,3,4)
#y=list(x)
#y.remove(3)
#x=tuple(y)
#print(x)

#x=(1,2,3)
#del x
#print(x)

#fruits=("apple","banana","cherry")
#(green,yellow,red)=fruits
#print(green)
#print(yellow)
#print(red)

#fruits=("apple","banana","cherry","melon")
#(green,yellow,*red)=fruits
#print(green)
#print(yellow)
#print(red)

#a=("a","b","c")
#b=(1,2,3)
#c=a+b
#print(c)

#a=("a","b","c")
#b=a*2
#print(b)

#1.replace an element in a tuple
#t=(10,20,30,40)
#x=list(t)
#x.remove(20)
#x.insert(1,25)
#t=tuple(x)
#print(t)

#2.add an element to a tuple
#t=(1,2,3)
#x=list(t)
#x.append(50)
#t=tuple(x)
#print(t)

#3.remove an element from a tuple
#t=(10,20,30,40)
#x=list(t)
#x.remove(30)
#t=tuple(x)
#print(t)

#4.add 5 to the list inside the tuple
#t=(1,[2,3],4)
#x=list(t)
#x.append(5)
#t=tuple(x)
#print(t)

#5.unpack into a,b,c and print them
#t=(10,20,30)
#(a,b,c)=t
#print(a)
#print(b)
#print(c)

#6.swap 2 nums using tuple unpacking
#a=5
#b=10
#(a,b)=(b,a)
#print(a)
#print(b)

#7.unpack with * operator
#t=(1,2,3,4,5)
#(a,b,*c)=t
#print(a)
#print(b)
#print(*c)

#8.ignore values while unpacking
#t=(10,20,30,40)
#(a,_,_,d)=t
#print(a)
#print(d)

#9.join 2 tuples
#t1=(1,2,3)
#t2=(4,5)
#t3=t1+t2
#print(t3)

#10.join tuple multiple times
#t=(1,2)
#t=t*3
#print(t)

#11.join tuple and list
#t=(1,2)
#l=[3,4]
#m=tuple(l)
#x=t+m
#print(x)

#12.predit the output
t=(1,2,3)
t+=(4,)
print(t)



 

