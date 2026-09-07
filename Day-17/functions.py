#Python Functions
'''
def gst(price):
    print("Original Price:",price)
    print("Final Price:", price+price*0.18)
    
gst(1000)
gst(4000)
gst(800)
gst(1890)


def table(num):
    print(num,"Table")
    print("-----------------")
    for i in range(11):
        print(num,"x",i,"=",num*i)
        
for i in range(1,20):
    table(i)

def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
        return "Not a leap year"
    
print(isleap(2012))
print(isleap(2020))
print(isleap(2002))
    


def prime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return "Not Prime"
    return "Prime"

print(prime(23))
print(prime(14))
print(prime(3))
        

#positional arrguments
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
    
display("sameer","sameer123@gmail.com","sameer@123")
display("sameer123@gmail.com","sameer","sameer@123")
display("sameer@123","sameer123@gmail.com","sameer",)



#keyword arrguments
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
    
display(name="sameer",email="sameer123@gmail.com",pwd="sameer@123")
display(name="sameer123@gmail.com",name="sameer",pwd="sameer@123")
display(pwd="sameer@123",email="sameer123@gmail.com",name="sameer",)

#default arrguments
def display(name,email,pwd=None):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
    
display("sameer","sameer123@gmail.com")
display("sameer123@gmail.com","sameer","sameer@123")


def display(*name):
    print("name:",name)
    
display("sameer")
display("sameer","sameer")
display("sameer","basha","shiak")
'''

def display(**names):
    print(names)
    
display(n1="sameer")
display(n1="sameer",n2="basha")