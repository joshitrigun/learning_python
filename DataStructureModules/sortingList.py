import bisect


def insertion_sort(ele):
    sorted_list = []

    for e in ele:
        bisect.insort(sorted_list, e)
        print(sorted_list)
    return sorted_list


ele = [2, 54, 64, 23, 15, 4, 9, 1]
s_list = insertion_sort(ele)
print(s_list)