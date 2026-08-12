Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=input()
narayana
a
'narayana'
a=(int(input()
       80
       
SyntaxError: '(' was never closed
a=(int(input())
   80
   
SyntaxError: '(' was never closed
a=int(input())
   
55
a
   
55
b=int(input())
   
56
b
   
56
f=float(input())
   
67.4
f
   
67.4
names="narayana","thota"
   
list(names)
   
['narayana', 'thota']
name="narayana"
   
list(name)
   
['n', 'a', 'r', 'a', 'y', 'a', 'n', 'a']
names=input().split(" ")
   
narayana sameer vijay
names
   
['narayana', 'sameer', 'vijay']
names=input().split("")
   
narayana sammer vijay
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    names=input().split("")
ValueError: empty separator
names=input().split()
   
narayana sameer vijay sailesh 
names
   
['narayana', 'sameer', 'vijay', 'sailesh']
tuple(names)
   
('narayana', 'sameer', 'vijay', 'sailesh')
set(names)
   
{'narayana', 'vijay', 'sameer', 'sailesh'}
name="narayana thota".split()
   
name
   
['narayana', 'thota']
courses=input()
   
python reasoning softskills
name.split()
   
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name.split()
AttributeError: 'list' object has no attribute 'split'
courses.split()
   
['python', 'reasoning', 'softskills']
names=tuple(input().split())
   
ramkrishna leela narayana
names
   
('ramkrishna', 'leela', 'narayana')
names=input().split()
   
names=input().split()
names=input().split()
   
balu narayana raviteja
tuple(names)
   
('balu', 'narayana', 'raviteja')
names=input().split()
   
baji narayana gowri
set(names)
   
{'baji', 'narayana', 'gowri'}
values=input().split()
   
1 2 3 4 5
values
   
['1', '2', '3', '4', '5']
map(int,values)
   
<map object at 0x000001BB6641BD30>
list(map(int,values))
   
[1, 2, 3, 4, 5]
tuple(map(int,values))
   
(1, 2, 3, 4, 5)
set(map(int,values))
   
{1, 2, 3, 4, 5}
values=list(map(int,input().split()))
   
1 2 3 4 5 
values
   
[1, 2, 3, 4, 5]
values=tuple(map(int,input().split()))
   
1 2 3 4 5
values
   
(1, 2, 3, 4, 5)
values=set(map(int,input().split()))
   
1 2 3 4 5
values
   
{1, 2, 3, 4, 5}
a,b=[1,2]
   
a
   
1
b
   
2
a,b,c=(1,22.3,"str")
   
a
   
1
b
   
22.3
c
   
'str'
name,age=input().split()
   
name,age=input().split()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    name,age=input().split()
ValueError: not enough values to unpack (expected 2, got 1)
name,age=input().split()
   
narayana 21
name
   
'narayana'
age
   
'21'
int(age)
   
21
a,b,c=list(map(float,input().split()))
   

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a,b,c=list(map(float,input().split()))
ValueError: not enough values to unpack (expected 3, got 0)
a,b,c=list(map(float,input().split()))
   
92.3 67.4 8.0
a
   
92.3
b
   
67.4
c
   
8.0
status=eval(input())
   
true
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
True
   
True
status
   
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    status
NameError: name 'status' is not defined
type(status)
   
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    type(status)
NameError: name 'status' is not defined
status=input()
   
status=input()
status=input()
True
   
SyntaxError: multiple statements found while compiling a single statement
status=input()
   
True
status
   
'True'
status=eval(input())
   

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    status=eval(input())
  File "<string>", line 0
    
SyntaxError: invalid syntax
status=eval(input())
(1,2,3,4,5)
   
SyntaxError: multiple statements found while compiling a single statement
status=eval(input())
(1,2,3,4,5)
   
SyntaxError: multiple statements found while compiling a single statement
status=eval(input())
   
(1,2,3,4,5)
status
   
(1, 2, 3, 4, 5)
status=eval(input())
   
[1,2,3,4,5]
status
   
[1, 2, 3, 4, 5]
status=eval(input())
{1:1,2:2,3:3}
   
SyntaxError: multiple statements found while compiling a single statement
>>> status=eval(input())
...    
status=eval(input())
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1
    status=eval(input())
          ^
SyntaxError: invalid syntax
>>> status=eval(input())
...    
{1:1,2:2,3:3}
>>> status
...    
{1: 1, 2: 2, 3: 3}
