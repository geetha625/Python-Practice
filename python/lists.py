#thislist=["apple", "banana", "cherry"]
#thislist[0] = "kiwi"
#print(thislist[1])

#thislist = ["apple", "banana", "cherry"]
#thislist[1:3] = ["watermelon", "mango"]
#print(thislist)

#1.#create a list of 5 nums
#mylist = [10, 20, 30, 40, 50]
#print(mylist)

#2.print first and last element
#mylist=[10,20,30,40,50]
#print(mylist[0])
#print(mylist[-1])

#3.change 3rd element value
#mylist=[10,20,30,40,50]
#mylist[2]=3
#print(mylist)

#4.print list using loop

#5.check type of list elements
#mylist=[1,2,3,4,5]
#print(type(mylist))


#1.create a list of 5 nums
#mylist=[1,2,3,4,5]
#print(mylist)

#2.add one num at the end
#mylist=[1,2,3,4,5]
#mylist.append(6)
#print(mylist)

#3.insert a num at index 2
#mylist=[1,2,3,4,5]
#mylist.insert(2,7)
#print(mylist)

#4.remove one element
#mylist=[1,2,3,4,5]
#mylist.remove(4)
#print(mylist)

#5.print all elements using loop
#mylist=[1,2,3,4,5]
#for i in mylist:
 #   print(i)

#6.check if 25 exists in the list
#mylist=[5,10,15,20,25]
#if 25 in mylist:
  #  print("yes")


         #list comprehension

#1.create a list of nums from 1 to 10 using list comprehension
#mylist=[1,2,3,4,5,6,7,8,9,10]
#newlist=[i for i in mylist]
#print(newlist)

#2.create a list that contains only even nums
#mylist=[1,2,3,4,5,6]
#newlist=[i for i in mylist if i%2==0]
#print(newlist)

#3.from the same list,create a new list of squares of all nums
#mylist=[1,2,3,4,5,6]
#newlist=[i*i for i in mylist]
#print(newlist)

#4.create a list of nums greater than 5
#nums=[2,4,6,8,10]
#newlist=[i for i in nums if i>5]
#print(newlist)

#5.convert the list into uppercase using list comprehension
#names=["python","java","c"]
#newlist=[i.upper() for i in names]
#print(newlist)

          #sort list

#6.sort the list in ascending order
#nums=[5,1,4,2,3]
#nums.sort()
#print(nums)

#7.sort the same list in descending order
#nums=[5,1,4,2,3]
#nums.sort(reverse=True)
#print(nums)

#8.sort the list without changing the original list
#nums=[7,3,9,1]
#newlist=[i for i in nums if sorted]
#print(nums)

#9.sort the list of strings alphabetically
#names=["banana","apple","cherry"]
#names.sort()
#print(names)

#10.create a new list of squares then sort the result in descending order
#nums=[3,1,4,2,5]
#newlist=[i*i for i in nums]
#newlist.sort(reverse=True)
#print(newlist)

#nums=[x for x in range(1,11)]
#print(nums)

#nums=[7,3,9,1]
#newlist=sorted(nums)
#print(newlist)


#wt is the diff b/w append() and extend()?
#append : it adds an element at the end of the list
#nums=[1,2,3]
#nums.append([4,5])
#print(nums)
#extend : it adds multiple elements
#nums=[1,2,3]
#nums.extend([4,5])
#print(nums)

#reverse a list without using reverse() or slicing
#nums=[1,2,3]
#rev=[]
#for i in nums:
#   rev.insert(0,i)
#print(rev)

#find the second largest element in a list
nums=[10,20,4,45,99]
largest=second=-1
for i in nums:
   if i >largest:
      second=largest
      largest=i
   elif i > second and i!=largest:second=i
print(second)


