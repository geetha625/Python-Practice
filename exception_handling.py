
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
print(safe_divide(10,0))      '''           # cannot divide

try:
    x=int(input("enter a num:"))
    print(10/x)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("zero error")
'''output :
enter a num:0
zero error'''



