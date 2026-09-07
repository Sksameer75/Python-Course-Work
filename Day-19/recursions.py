'''
#10 to 1
def display(n):
    if n == 11:
        return
    display(n+1)
    print(n)
display(1)

def display(s,n):
    if n == len(s):
        return
    display(s,n+1)
    print(s[n])
    
display("Codegnan",0)

def display(s,i,w):
    if len(s)-w+1 == i:
        return
    print(s[i:i+w])
    display(s,i+1,w)
    
s=input("Enter the string:")
w = int(input("Enter the widht:"))
display(s,0,w)
   
 
def display(l,i):
    if i == len(l):
        return 0
    return l[i] + display(l,i+1)
    
lis = [1,2,3,4,5]
print(display(lis,0))


def display(n):
    if n == 0:
        return 0
    return n%10 + display(n//10)
n = 12345
print(display(n))


def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
    
print(fact(5))


n = int(input("Enter the number:"))
if n == 1:
    print(0)
elif n == 2:
    print(0,1)
else:
    a,b = 0,1
    print(a,b,end=" ")
    for i in range(n-2):
        a,b = b,a+b
        print(b,end=" ")
'''


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(20):
    print(fib(i))