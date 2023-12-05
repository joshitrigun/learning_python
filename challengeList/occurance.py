L1 = ['A', 'B', 'C', 'E', 'I', 'A', 'B', 'D', 'E', 'F', 'G', 'I']

result = []
for i in L1:
    if i not in result:
        result.append(i)
        count = L1.count(i)
        result.append(count)

print(result)