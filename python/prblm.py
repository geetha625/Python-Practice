#sum of all numbers in a list using for loop
arr = [3, 5, 7, 2]
total = 0
for num in arr:
    total = total + num
print(total)#17

#print the square of the numbers from 1 to n
n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i*i,end=" ")#1 4 9 16 25