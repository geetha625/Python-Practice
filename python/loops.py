#print all even nums from 1 to 50
#for i in range(1,51):
 #   if i%2==0:
 #    print(i)

#find sum of nums from 1 to n using loop
#n=10
#sum=0
#for i in range(1,n+1):
#    sum+=i
#print(sum)

#reverse a num using loop
#num=1234
#rev=0
#while num>0:
#    digit=num%10
#    rev=rev*10+digit
#    num=num//10
#print(rev)

#count digits using loop
#num=1233456
#count=0
#while num>0:
#    num=num//10
#    count+=1
#print(count)

#check if a num is palindrome using loop
num=121
original=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if original==rev:
    print("palindrome")
else:
    print("not a palindrome")
