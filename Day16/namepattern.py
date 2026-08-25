'''
#D
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#E
n = int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i == m:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


#F
n = int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == m:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

#C
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

    
#G
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or (i == m and j >= 1) or j == n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
    


#H
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j == 0 or i == m or j == n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

#I
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == n//2:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


#Z
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i+j == n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

    
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or i+j == n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

#X
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i == j or i + j == n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

    
#K
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j == 0 or (i==m and j<=m) or (i==j and i>=m) or (i+j == n-1 and i<=m):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


#T
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == n//2:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


#J
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == n//2 or (i == n-1 and j == n//2):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

#Q
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1 or (i == j and i+j>m):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#V
n=int(input("Enter the number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == n//2 or (i==n-1 and i<=m):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


