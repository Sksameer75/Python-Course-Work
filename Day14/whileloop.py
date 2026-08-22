'''
i = 0
while i <= 10:
    print(i)
    i = i+1
    
'''
'''
i = 10
while i > 0:
    print(i)
    i = i-1


s = "while loop"
i = len(s)-1
while i>0:
    print(s[i])
    i=i-1



n = 8765
while n>0:
    print(n%10,end="")
    n=n//10
    
      
n = 98765432456
s=0
while n>0:
    s=s+n%10
    n=n//10
print(s)
    


n = 34567
res = 0
while n>0:
    res = res*10+n%10
    n=n//10
print("Reversed Number:",res)
    

n = 876543456
res=0
while n>0:
    rem = n%10
    if rem%2==0:
        res = res + rem
    n=n//10
print(res)


l = [2,3,5,7,0,3,5,0,4,0,3,0,6,0,35,64,34,0]
while 0 in l:
    l.remove(0)
print(l)

'''

l = [2,3,6,76,12,4,1,5,61,4,5,2,23]
i,j=0,len(l)-1
while i<=j:
    if i == j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i=i+1
    j=j-1

