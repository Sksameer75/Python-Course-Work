'''
#Local Variable
def display():
    n = 10
    print("Inside Function", n)
display()

#Global Variable
def display():
    print("Inside Function", n)

n =30
display()
print("Outside fuction",n)

#Global Scope
def display():
    global n
    n = 10
    print("Inside Function", n)
n = 20
display()
print("Outside Function",n)


def display():
    global n
    n = n+10
    print("inside function", n)
    
n = 10
display()
print("Outside Function",n)


def display():
    course = 'PFS'
    def update(): 
        nonlocal course
        course = 'JFS'
        print("Inner Function",course)
    update()
    print("Outer Function",course)
    
display()

#if we use method names as variable so they act as variable instead of a methon or function so 
#we can't use them as a variable

l = [1,2,3,4,5]
print(sum(l))

print = 10
print(print)

'''

