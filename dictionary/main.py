# # # dict1 = dict(((1, 3), (3, 5), (5, 7)))
# # #
# # # dict2 = dict()
# # #
# # # dict3 = dict(((1, 2), (2, 4)))
# #
# #
# #
# # # d4 = dict(zip((1, 2)))
# #
# # # d5 = {
# # #         'A': 'apple',
# # #         'B': 'ball',
# # #         'C': 'cat'
# # # }
# # # dic = dict()
# # # for x in range(1, 5):
# # #     dic[x] = x**2
# # #
# # # print(dic)
# #
# # tupdict = dict(([1, 3], [2, 4], [3, 6]))
# # print(tupdict)
# #
# #
# # dic_Couple = dict(({'ab', 'cd', 'ef'}))
# # print(dic_Couple)
# #
# # l1 = [(1, 2), (3, 4), (5, 7)]
# # print(dict(l1))
# #
# #
#
#
#
# l2 = ('12', '34', '56', '78', '90')
#
# dict33 = dict(zip(l1, l2))
# print(dict33)

# l1 = ['a', 'b', 'c', 'd', 'e']
#
# dicenumerate = dict(enumerate(l1))
#
# print(dicenumerate)


# dict11 = {x: x**2 for x in range(1, 10)}
# print(dict11)
#
# dict12= dict((x, x**2) for x in range(1, 10))
# print(dict12)
#
# l1 = [1, 2, 3]
# l2 = ('12', '34', '56', '78', '90')
#
# dictA = dict((x, y) for x, y in zip(l1, l2))
# print(dictA)
# dictB = {x: y for x, y in zip(l1, l2)}
# print(dictB)
#
# dictC= {x:y for x, y in enumerate(l2)}
# print(dictC)
#
# dictA1= {x:y for x, y in enumerate(l1)}
# print(dictA1)

D = dict()

for x in enumerate(range(2)):

    D[x[0]] = x[1]

    D[x[1]+7] = x[0]

print(D)