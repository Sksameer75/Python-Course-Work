Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=67.4
c="codegnan"
print("a=",a,"b=",b,"c=",c)
a= 10 b= 67.4 c= codegnan
print("a=",a,"b=",b,"c=",c,sep=' ')
a= 10 b= 67.4 c= codegnan
print("a=",a,"b=",b,"c=",c,sep='\n')
a=
10
b=
67.4
c=
codegnan
print("a=",a,"b=",b,"c=",c,sep='\t')
a=	10	b=	67.4	c=	codegnan
a=	10	b=	67.4	c=	codegnan
SyntaxError: invalid syntax

print(f'a={a} b={b} c={c})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f'a={a} b={b} c={c}')
      
a=10 b=67.4 c=codegnan
print('a=%d b=%f c=%s(a,b,c))
      
SyntaxError: unterminated string literal (detected at line 1)
print(f'a=%d b=%f c=%s'(a,b,c))
      
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(f'a=%d b=%f c=%s'(a,b,c))
TypeError: 'str' object is not callable
print(f'a=%s b=%f c=%s'(a,b,c))
      
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(f'a=%s b=%f c=%s'(a,b,c))
TypeError: 'str' object is not callable
print(f'a=%d b=%s c=%s'(a,b,c))
      
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(f'a=%d b=%s c=%s'(a,b,c))
TypeError: 'str' object is not callable
print(f'a=%s b=%s c=%s'(a,b,c))
      
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(f'a=%s b=%s c=%s'(a,b,c))
TypeError: 'str' object is not callable
print('a=%d b=%f c=%s'(a,b,c))
      
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print('a=%d b=%f c=%s'(a,b,c))
TypeError: 'str' object is not callable
>>> print('a=%s b=%s c=%s'%(a,b,c))
...       
a=10 b=67.4 c=codegnan
>>> print('a={} b={} c={}'.format(a,b,c))
...       
a=10 b=67.4 c=codegnan
>>> print('a={} b={} c={}'.format(b,c,a))
...       
a=67.4 b=codegnan c=10
>>> print('a={0} b={1} c={2}'.format(a,b,c))
...       
a=10 b=67.4 c=codegnan
>>> a=10 b=67.4 c=codegnan
...       
SyntaxError: invalid syntax
>>> print('a={2} b={0} c={1}'.format(a,b,c))
...       
a=codegnan b=10 c=67.4
