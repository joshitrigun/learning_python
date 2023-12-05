import array

ar1 = array.array('i',[10,20,30,40,50])
print(ar1)

str1 = b'abcdef'

ar2 = array.array('b', str1)
print(ar2)

print(ar2[0])

print(ar2[1:4])
ar2.append(103)
print(ar2)

print(ar2.index(103))
