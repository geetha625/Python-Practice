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
#num=121
#original=num
#rev=0
#while num>0:
#    digit=num%10
#    rev=rev*10+digit
#    num=num//10
#if original==rev:
#    print("palindrome")
#else:
#    print("not a palindrome")

#n=5
#for i in range(1,n+1):
#    print(i,end=" ")       # 1 2 3 4 5

# STRING METHOD

#n="123"
#rev=""
#for i in n:
#    rev=i+rev
#print(rev)

"NUMBER METHOD"   "while loop"

#n=123
#rev=0
#while n>0:
#    digit=n%10
#    rev=rev*10+digit
#    n=n//10
#print(rev)     #321

"PALINDROME USING WHILE LOOP"

#n=121
#original=n
#rev=0
#while n>0:
#    digit=n%10
#    rev=rev*10+digit
#    n=n//10
#if original==rev:
#   print(True)
#else:
#   print(False)   # True

"ARMSTRONG NUMBER"
#n=153
#original=n
#sum_digits=0
#while n>0:
#    digit=n%10
#    sum_digits+=digit**3
#    n=n//10
#if original==sum_digits:
#    print(True)
#else:
#    print(False)       # True

" find largest number"
#n=58392
#large_num=0
#while n>0:
#    digit=n%10
#    if digit>large_num:
#        large_num=digit
#    n=n//10
#print(large_num)  # 9

# NOTE: for numbers problems must use 
# digit extraction(digit=n%10) for separating nums
# remove digit(n=n//2)

# SUM OF DIGITS

#n=458
#sum_=0
#while n>0:
#    digit=n%10
#    sum_+=digit
#    n=n//10
#print(sum_)          # 17

# COUNT DIGIT

#n=90210
#count_=0
#while n>0:
#    digit=n%10
#    count_+=1
#    n=n//10
#print(count_)       # 5

# REVERSE NUMBER

#n=305
#rev=0
#while n>0:
#    digit=n%10
#    rev=rev*10+digit
#    n=n//10
#print(rev)         # 503

# PALINDROME NUMBER

#n=1221
#original=n
#rev=0
#while n>0:
#    digit=n%10
#    rev=rev*10+digit
#    n=n//10
#if original==rev:
#    print(True)
#else:
#    print(False)       # True

# EVEN OR ODD

#n=76421
#even_digit=0
#odd_digit=0
#while n >0:
#    digit=n%10
#    if digit%2==0:
#        even_digit+=1
#    else:
#        odd_digit+=1
#    n=n//10
#print("even : ",even_digit)       # 3
#print("odd: ",odd_digit)          # 2

'''n=482
while n>0:
    digit=n%10
    print(digit)
    n=n//10
OUTPUT:
2
8
4'''

# COUNT DIGITS > 5

#n=76952
#count_=0
#while n>0:
#    digit=n%10
#    if digit>5:
#        count_+=1
#    n=n//10
#print(count_)    # 3

# PRODUCT

''' n=234
product_=1
while n>0:
    digit=n%10
    product_*=digit
    n=n//10
print(product_) '''     # 24

''' num=1
while num<6:
    print(num)
    num+=1 '''

''' num=1
while num<6:
    print(num)
    if num==3:
        break
    num+=1
OUTPUT :
1
2
3 '''

''' num=0
while num<6:
    num+=1
    if num==3:
        continue
    print(num)
OUTPUT :
1
2
4
5
6 '''







    


