#no of rows=n
#to print in each row :stars,nums,alphabets

#square
#n=4
#for i in range(n):
#    for j in range(n):
#        print("*",end="")
#    print()

#n=5
#for i in range(1,n+1):
#    print("*"*i)

#n=5
#for i in range(1,n+1):
#    for j in range(1,i+1):
#        print(j,end="")
#    print()

#n=5
#for i in range(1,n+1):
#    for j in range(2,i+2):
#        print(j,end="")
#    print()

#n=5
#for i in range(1,n+1):
#    for j in range(3,i+3):
#        print(j,end="")
#    print()

# reverse pattern printing         
'''n=5
for i in range(1,n+1):
    print("*"*(n-i+1)) '''       #each iteration to count stars use (n-i+1)

'''n=4
for i in range(1,n+1):
    print("*"*(n-i+1)) '''

# hallow square pattern
'''n=5
for i in range(n):
    spaces=" "*(n-2)     # spaces between stars
    if i==0 or i==n-1:    #rows
        print("*"*n)
    else:
        print("*"+spaces+"*")'''

'''n=4
for i in range(n):
    spaces=" "*(n-2)
    if i==0 or i==n-1:
        print("*"*n) 
    else:
        print("*"+spaces+"*")'''

# same num in row             - row num = num to print
# one loop for rows   - i=row num
# one loop for nums inside each row     - j=num to print
'''n=4
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
# output:
1
2 2 
3 3 3
4 4 4 4 '''

'''n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print() '''
# output :
'''1
2 2 
3 3 3
4 4 4 4 
5 5 5 5 5'''

# increasing number pattern 
'''n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
1 
1 2 
1 2 3
1 2 3 4 '''

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


                                 


