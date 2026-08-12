l=[]
l=list()
print(type(l))
lst=[1,2.34,"str", True, [1,2,4], (2,4,5,4), {1,2,4}, {1:1,3:4,5:5}, 3+8j]
print(lst)
a=[1,2]
b=[3,4]
print(a+b)
print(a*2)
print(1 in a)
print(3 in a)
print(1 not in a)
print(3 not in a)
c=[1,2,3,4,5,6,7,8]
print(c[1:])
print(c[0::-1])

c=[1,2,3,4,5,6,7,8]
print(c[2:8:2])
print(c[8:2:-1])
lst=[1,2,3,4,5]
lst.append(6)
lst.extend([5,6])
lst.insert(4,5)

lst=[1,2,3,4,5,5]
print(lst)
lst.remove(5)
print(lst.pop(0))
print(lst)
lst.clear()
print(lst)

del lst1[0]
print(lst1)

lst1=[1,2,3,4,5,5]
print(lst1.index(5))
print(lst1.count(5))

lst1=[5,3,1,8,6,7,2]
lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)
print(sorted(lst1))

lst1=[1,2,3,4,5,5]
lst2=lst1.copy()
print(lst2)
