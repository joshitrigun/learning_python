from collections import Counter

List1 = ['Tripti', 'Trigun', 'Trija', 'Tripti', 'Trija', 'Tripti']

c = Counter(List1)


# print(c['Tripti'])
# print(c.get('Trija'))
# print(c.keys())
# print(c.values())

c.update({'Sanu': 3})
# print(c.keys())
# print(c.values())

c.update({'Rita': 4})
# print(c.keys())
# print(c.values())
#
# print(c.elements())
#
# for i in c.elements():
#     print(i)

print(c.most_common(3))
print(c)