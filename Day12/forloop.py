#for loops
#----------

s = 'python programming'
for i in s:
    print(i)

l = [1,2,3,4,5,6]
for num in l:
    print(num)

prices = (9875,343,5678,334,5678)
for price in prices:
    print(price)

names = {'sameer','narayana','sailesh'}
for i in names:
    print(i)


d = {1:2,2:4,3:6,4:8,5:10}
for i in d:
    print(i,d[i])


#Range function in loops

for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(5,0,-1):
    print(i)
    

s = "python programming"
for i in range(len(s)):
    print(i,s[i])

s = (345,234,534,646,764,423)
for i in range(len(s)):
    print(i,s[i])
    
s = "sameer basha"
for i in enumerate(s):
    print(i[0],i[1])

d={1:1,2:2,3:6,4:8}
for i in enumerate(s):
    print(i)

for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)

l = [12,13,15,16,18]
n=26
for i in l:
    if i == n:
        print(n,"found")
        break
else:
    print(n,"not found")
    
pin = 1234
for i in range(5):
    epin = int(input("Enter the pin:"))
    if epin == pin:
        print("Phone Unlocked")
        break
    else:
        print("Invalid Pin")
else:
    print("Try after 30 Seconds")



n = 17
for i in range(2,n//2+1):
    if n%i == 0:
        print("Not Prime Number")
        break
else:
    print("Prime Number")




