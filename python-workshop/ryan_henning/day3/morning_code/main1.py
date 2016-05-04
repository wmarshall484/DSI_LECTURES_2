from myset import myset

s = myset([1, 5, 8])
s.add('ryan')
s.discard(5)
s.add(3)
s.add('bob')

print s.to_list()

print (8 in s)
print (6 in s)

for item in s:
    print item

t = myset()
t.add(8)
t.add(('dog', 'cat'))
t.add('bob')

union = (s | t)
inter = (s & t)

print type(inter)

print union.to_list()
print inter.to_list()

print inter

