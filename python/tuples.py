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
t=(10,20,30)
total=0
for i in t:
    total+=i
print(total)
    
 

