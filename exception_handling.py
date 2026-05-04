
'''try:
    x=int(input())
    print(10/x)
except:
    print("error occured")
output:
error occured

try:
    x=int(input())
    print(10/x)
except ZeroDivisionError:
    print("error occured")
output:
error occured

try:
    x=int(input())
    print(10/x)
except ValueError:
    print("error occured")
output:
error occured

try:
    print("hello")
finally:
    print("done")
OUTPUT:
hello
done

x=5
try:
    y=10/x
except:
    print("error occured")
else:
    print(y)                             # 2.0

def safe_divide(a,b):
    try:
        return a/b
    except:
        return "cannot divide"
print(safe_divide(10,4))                 # 2.5
print(safe_divide(10,0))               # cannot divide

try:
    x=int(input("enter a num:"))
    print(10/x)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("zero error")
output :
enter a num:0
zero error
enter a num:5
2.0     

# list index handling
arr=[1,2,3]
try:
    index=int(input("enter the index:"))
    print(arr[index])
except IndexError:
    print("out of range error")
output:
enter the index:3
out of range error
enter the index:1
2          

# file handling exception
try:
    with open("data.txt") as f:
     print(f)
except FileNotFoundError:
    print("file not found")              # file not found

# custom error msg
try:
   x=10/0
except ZeroDivisionError:
   print("error invalid operation")        # error invalid operation

try:
    num=int(input("enter a num:"))
    print(100/num)
except (ValueError,ZeroDivisionError):
    print("invalid operation")
output:
enter a num:0
invalid operation
enter a num:5
20.0                     

# output prediction
try:
    print(1)
    print(10/0)
    print(2)
except ZeroDivisionError:
    print(3)
finally:
    print(4)
output:
1
3
4    

try:
    return 1
finally:
    return 2
output:
SyntaxError: 'return' outside function    '''

def Test():
 try:
    return 1
 finally:
    return 2
print(Test())

''' # exception in finally
try:
    print("A")
finally:
    print(10/0)
output:
ZeroDivisionError: division by zero             

# raise keyword   - used to manually create/throw an exception  (force)
age=16
if age<18:
    raise Exception("Not Eligible")           # Exception: Not Eligible

# custom exception   - to create own error type
# are user defined errors for specific conditions
class InvalidMarksError(Exception):
    pass
marks=120
if marks>100:
    raise InvalidMarksError("marks cannot be more than 100")
output:
InvalidMarksError: marks cannot be more than 100 '''




