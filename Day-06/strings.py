f=input("enter  string")
l=input("enter l name")
#string concatenation
c=f+l
print(c,sep='@')
#string repetation
print(c*5)

#indexing
names='narayana sameer vijay sailesh'
print(names[0:8])
print(names[::-1])
print(names[9:16])
print(names[-1:-8:-1])
print("karthik" in names)
print('narayana' not  in names)

#functions of str
name=" narayana"
print(len(name))
print(ord(name[1]))
print(chr(90))
print(sorted(name))
print(min(name)

#case methods in string
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

#align methods
name="narayana"
print(name.center(20,'-'))
print(name.center(20,'$'))
print(name.ljust(20,'&'))
print(name.rjust(20,'&'))
print('67'.zfill(3))

s="python programmming"
print(s.find('python'))
print(s.find('programming'))
print(s.find('r'))
print(s.rfind('r'))
print(s.index("p"))
print(s.rindex("p"))
print(s.count("p"))
print(s.replace('p','$'))
print(s.replace('programming','language'))
print(s.maketrans('aeiou','!@#$%'))
print(s.translate({97: 33, 101: 64, 105: 35, 111: 36, 117: 37}))

a="nothing 😊"

print(a.encode())
print(a.decode(b'nothing \xf0\x9f\x98\x8a'))

s=' narayana thota'
print(s.strip())
print(s.lstrip())
n=' narayana thota '
print(n.rstrip())
print(s.replace(' ',''))

n='om-sada-siva-venkata-narayana'
print(n.split('-'))
print(n.split('-',1))
print(n.rsplit('-',))
print(n.rsplit('-',2))

n='om\nsada-siva-venkata-narayana'
print(n)
print(n.splitlines())

lst=["om","sada","siva","venkata","narayana"]
print(''.join(lst))
print(' '.join(lst))
print('--'.join(lst))
tup=("om","sada","siva","venkata","narayana")
print('--'.join(tup))
s={"om","sada","siva","venkata","narayana"}
print('--'.join(s))

p='working.on.strings'
print(p.partition('.'))
print(p.rpartition('.'))

#testing methods
a='narayanathota'
print(a.startswith('n'))
print(a.startswith('a'))
print(a.endswith('thota'))
print(a.endswith(a[::-1]))

n="narayanathota23"
m=' ' 
print(n.isalnum())
print(n.islower())
print(n.isupper())
print(m.isspace())
print(n.istitle())
print(n.isidentifier())
'2554656'.isdecimal()
'5656#'.isdecimal()
'5656#'.isnumeric()



























      



        
