L1 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

L2 = []

for i in range(4):
    S = []
    for j in range(3):
        S.append(L1[j][i])
    L2.append(S)

print(L2)