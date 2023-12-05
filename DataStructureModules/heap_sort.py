import heapq


def heap_sort(elements):
    heapq.heapify(elements)
    # print(elements)

    sorted_list = []
    for i in range(len(elements)):
        x = heapq.heappop(elements)
        sorted_list.append(x)
    return sorted_list

elements = [12, 14, 5, 6, 7, 1, 8, 9]

print(heap_sort(elements))