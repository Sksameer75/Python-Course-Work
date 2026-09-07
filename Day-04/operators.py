Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#python operators
#1.Arthimetic operators
a=10
b=20
a+b
30
a-b
-10
a**a
10000000000
a*a
100
a/b
0.5
a//b
0
a%b
10
#2.comparison operator
a>b
False
a<b
True
a>=b
False
a<=b
True
a==b:
    
SyntaxError: invalid syntax
a==b
False
a1=b
a!=b
True
#3.Assignment operators
a=10
a+=20
a-=10
a=10
a
10
a
10
a+=10
a
20
a-=10
a
10
a*=10
a
100
a//=30
a
3
a/=30
a
0.1
a*=2
a
0.2
a=30
a%=10
a
0
a=80
a%%=10
SyntaxError: invalid syntax
a%=10
a
0
#Realational operation

email=True
passowrd=fale
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    passowrd=fale
NameError: name 'fale' is not defined. Did you mean: 'False'?
password=False
email and password
False
login=false
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    login=false
NameError: name 'false' is not defined. Did you mean: 'False'?
login=False
p=True
login or p
True
's' in "aeiou'
SyntaxError: unterminated string literal (detected at line 1)
's' in 'aeiou'
False

's' not in 'aeiou'
True
5%3==0 and 7%6==0
False
4%2==0 or 5%3==0
True
#membership operator
s='python programming'
'pytho' in s
True
'program' not in s:
    
SyntaxError: invalid syntax
'program' not in s
False
l=[92,67,80]
92 in l
True
92 not in l
False
t=(92,67,80)
67 not in t
False
76 not in t
True
80 in t
True
s={92,67,80}
43 not in s
True
67 in s
True
67 not in s
False
d={'name':'narayana','age':21,'course':'fullstack'}
narayana in d
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    narayana in d
NameError: name 'narayana' is not defined
name in d
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
"name" in d
True
"narayana" not in d
True
"name" not in d
False
False
False
#5.identical operators
l=[1,2,3,4]
m=[1,2,3,4]
id(1)
140717465483704
id(m)
2560776343872
l==m
True
l is m
False
n==m
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    n==m
NameError: name 'n' is not defined
n=m
>>> m is n
True
>>> 11 & 12
8
>>> 12 | 11
15
>>> 12 >> b
0
>>> 12 >> 13
0
>>> 12 << 15
393216
>>> ~2
-3
>>> ~-3
2
>>> ~*3
SyntaxError: invalid syntax
