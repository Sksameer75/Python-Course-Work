'''
#Pass by variable
#int
def display(n):
    n+=10
    print("Inside Function",n)
n = 10
display(n)
print("Outside Function", n)

#float
def display(n):
    n+=10.3
    print("Inside Function",n)
n = 10.3
display(n)
print("Outside Function", n)

#complex
def display(n):
    n+=10
    print("Inside Function",n)
n = 10+3j
display(n)
print("Outside Function", n)

#string
def display(n):
    n+=" Language"
    print("Inside Function",n)
n = "Python"
display(n)
print("Outside Function", n)

#tuple
def display(n):
    n.(5,4)
    print("Inside Function",n)
    
n = (1,2,3,4)
display(n)
print("Outside Function", n)


#List
def display(n):
    n.append(5)
    print("Inside Function",n)
    
n = [1,2,3,4]
display(n)
print("Outside Function", n)


#set
def display(n):
    n.add(5)
    print("Inside Function",n)
    
n = {1,2,3,4}
display(n)
print("Outside Function", n)

#Dictionary
def display(n):
    n[5] = 6
    print("Inside Function",n)
    
n = {1:2,2:3,3:4,4:5}
display(n)
print("Outside Function", n)

'''



