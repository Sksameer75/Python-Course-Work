Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #touples in python
>>> t = ()
>>> t = tuple()
>>> t = (1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> t = (1)
>>> t
1
>>> t = (1,)
>>> t
(1,)
>>> #Allows duplicates
>>> t = (1,4,5,1,1,1)
>>> t
(1, 4, 5, 1, 1, 1)
>>> t  = (1,2.3, "str", [1,2,3], (1,2,3), {1,2,4},{1:1,2:2,3:3}, True)
>>> t
(1, 2.3, 'str', [1, 2, 3], (1, 2, 3), {1, 2, 4}, {1: 1, 2: 2, 3: 3}, True)
>>> type(t)
<class 'tuple'>
(1,2,3)+(4+5+6)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    (1,2,3)+(4+5+6)
TypeError: can only concatenate tuple (not "int") to tuple
#concatenatino
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
#repetation
(1,2,4)*3
(1, 2, 4, 1, 2, 4, 1, 2, 4)
t
(1, 2.3, 'str', [1, 2, 3], (1, 2, 3), {1, 2, 4}, {1: 1, 2: 2, 3: 3}, True)
t[1]
2.3
t[-1]
True
t[-3]
{1, 2, 4}
t[2]
'str'
#slicing
t[1:5]
(2.3, 'str', [1, 2, 3], (1, 2, 3))
t[3:7]
([1, 2, 3], (1, 2, 3), {1, 2, 4}, {1: 1, 2: 2, 3: 3})
#member ship
2.3 in t
True
'str' in t
True
True in t
True
False in t
False
#tuple functions
t = (3,4,32,4,5,66,5,6,65,44,3,32,45,322)
t
(3, 4, 32, 4, 5, 66, 5, 6, 65, 44, 3, 32, 45, 322)
sorted(t)
[3, 3, 4, 4, 5, 5, 6, 32, 32, 44, 45, 65, 66, 322]
max(t)
322
min(t)
3
sum(t)
636
len(t)
14
t.index(44)
9
t.find(44)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t.find(44)
AttributeError: 'tuple' object has no attribute 'find'
t.count(4)
2
t.any
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t.any
AttributeError: 'tuple' object has no attribute 'any'
t.any()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    t.any()
AttributeError: 'tuple' object has no attribute 'any'
t = (1,2,4,[4,6,7])
t
(1, 2, 4, [4, 6, 7])
t[4].append(10)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t[4].append(10)
IndexError: tuple index out of range
t[3].append(10)
t
(1, 2, 4, [4, 6, 7, 10])
