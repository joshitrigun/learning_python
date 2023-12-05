import heapq

def kth_largest(element, k):
    sorted_list = []

    for e in element:
        heapq.heappush(sorted_list, -e)
    # print(sorted_list)

    for i in range(k-1):
        heapq.heappop(sorted_list)

    return -heapq.heappop(sorted_list)


element = [5, 12, 34, 6, 54, 34, 90, 73, 82]


print(kth_largest(element, 3))