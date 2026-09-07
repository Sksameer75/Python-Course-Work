
for i in range(5):
    for j in range(5):
        print((i+j)%2,end="")
    print()
        

for i in range(5):
    for j in range(5):
        print(i+j,end=" ")
    print()

c = 1
for i in range(5):
    for j in range(5):
        print(c,end=" ")
        c = c+1
    print()
    
    
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()



for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
        
    print()

n=7
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
    



n = int(input("Enter the size:"))
for i in range(n):
    for sp in range(i):
        print(' ',end=" ")
    for j in range(n-i):
        print("*",end='')
    print()
   

 
n = int(input())
m = n//2

for i in range(n):
    if i <= m:
        print("* "*(i+1),end=" ")
    else:
        print("* "*(n-1),end=" ")  
    print()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        