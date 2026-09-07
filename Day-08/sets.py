Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python set
s = set()
type(s)
<class 'set'>
s = {1,2,3,4,5,6,23,4,3,565,443,5,43,3,32,22}
s
{32, 1, 2, 3, 4, 5, 6, 43, 565, 22, 23, 443}
s = {1,1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s.add(12.3)
s.add('str')
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add((1,2,3))
s.add({1:1,2:3})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.add({1:1,2:3})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(False)
s
{False, 1, (1, 2, 3), 12.3, 'str'}
a = {1,2,3,4,5}
b = {3,5,7,8,9}
2 in a
True

20 in a
False
9 not in a
True
a - b
{1, 2, 4}
b - a
{8, 9, 7}
a ^ b
{1, 2, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5}
b
{3, 5, 7, 8, 9}
{1}<=a
True
{1,2,3}<=a
True
{1,24,5,3}<a
False
{34,5,2,3}>=a
False
a>={1,2}
True
a>={45,3,3,2,4}
False
a = {12,34,5,6,33,7,8,9}
a
{33, 34, 5, 6, 7, 8, 9, 12}
sorted(a)
[5, 6, 7, 8, 9, 12, 33, 34]
max(a)
34
min(a)
5
len(a)
8
a.index(a)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
a = {1,2,3}
b = a
b.add(4)
a
{1, 2, 3, 4}
b
{1, 2, 3, 4}
c
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c
NameError: name 'c' is not defined
c = a.copy(b)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    c = a.copy(b)
TypeError: set.copy() takes no arguments (1 given)
c = b.copy()
c
{1, 2, 3, 4}
c.add(5)
c
{1, 2, 3, 4, 5}
a
{1, 2, 3, 4}
b
{1, 2, 3, 4}
a.add(100)
a
{1, 2, 3, 100, 4}
a.add(105)
a
{1, 2, 3, 100, 4, 105}
a
{1, 2, 3, 100, 4, 105}
a.add(40)
a.remove(100)
a
{1, 2, 3, 4, 40, 105}
a.remove(105)
a.remove(105)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.remove(105)
KeyError: 105
>>> a.pop()
1
>>> a
{2, 3, 4, 40}
>>> a.discard(100)
>>> a
{2, 3, 4, 40}
>>> a = forzenset({2,4,3,2})
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a = forzenset({2,4,3,2})
NameError: name 'forzenset' is not defined. Did you mean: 'frozenset'?
>>> a = frozenset({2,4,3,2})
>>> a
frozenset({2, 3, 4})
