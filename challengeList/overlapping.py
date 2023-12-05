L1 = [10, 14, 12, 6, 9, 8, 4, 15]

L2 = [6, 19, 15, 3, 13, 16, 7, 21]

L3 = []

for i in L1:
    if i in L2:
        L3.append(i)

    # for j in range(len(L2)):
    #     if L2[j] == L1[i]:
    #         L3.append(i)

print(L3)
# for i in range(len(L1)):
#     indx = L2.index(L1[i])
#
#     if i + indx < index1+index2:
#         index1 = i
#         index2 = indx
#
# print(L1[index1], index1+index2)