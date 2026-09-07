#Python Dictionary
'''
d = {}
print(type(d))

d = {1:4,2:8,3:13}
print(d)'''

d = {}
d[1]=1
d[12.4] = 1
d['str'] = 1
d[(1,2,3)] = 1
d[(2+3j)] = 1
d[True] = 1
d[False] = 1
d[frozenset(1,2,3,40)] = 1
print(d)

