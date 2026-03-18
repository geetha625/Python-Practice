
'''n=int(input("enter a number:"))    
if n>0 and (n&(n-1)==0):
    print("yes")
else:
    print("false")'''

def isPowerofTwo(n):
    if n<=0:
        return False
    return (n&(n-1))==0
n=int(input("enter a num:"))
print(isPowerofTwo(n))

















