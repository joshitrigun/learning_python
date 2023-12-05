import array

def find_duplicate(nums):
    num_set = set()

    for n in nums:
        if n in num_set:
            return n
        else:
            num_set.add(n)
    else:
        return -1

arr = array.array('i', [2, 3, 4, 5, 6 ,7 ,8, 5, 4, 3])
print(find_duplicate(arr))