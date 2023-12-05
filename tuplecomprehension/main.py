# l1 = [x for x in range(0, 10)]
#
# print(l1)
# # t1 = (x for x in range(0, 10))
# t1 = tuple(x for x in range(0, 10))
# print(t1)
#
# t2 = (*(x for x in range(10)),)
# print(t2)
#
# t3 = (*(x for x in range(0, 10, 2)),)
# print(t3)
#
# t4 = (*(x for x in 'python'),)
# print(t4)
#
# t5 = (*(x for x in 'PythON' if x.islower()),)
# print(t5)
#
# t6 = tuple(x for x in 'PYthoN' if x.islower())
# print(t6)
#
# t7 = tuple(x**2 for x in (1, 2, 3, 6))
# print(t7)

# t8 = (1, 2, 3, 4, 4, 5, 6, 7, 8)
# print(t8.count(4))

T9= ('python',[10,20,30],(40,50))
print(T9[1][1])
