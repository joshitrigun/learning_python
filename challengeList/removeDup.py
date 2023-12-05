# l1 = [3, 5, 3, 5, 1, 2, 4, 5, 6, 7, 8, 9, 7, 6, 3, 1, 6, 7, 8]
#
#
# l2 =[]
#
# # for x in l1:
# #     if x not in l2:
# #         l2.append(x)
# #
# # print(l2)
#
# [l2.append(l) for l in l1 if l not in l2]
#
# print(l2)

t = [1, 2, 3, 1, 2, 3, 5, 6, 7, 8]

print(id(t))

print(t)


print('list(set(t))' ,list(set(t)))
print(id(t))

