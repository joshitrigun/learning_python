import array


def missing_num(given_list):
    start = given_list[0]
    end = given_list[len(given_list) - 1]

    actual_list = list(range(start, end + 1))

    actual_sum = sum(actual_list)
    given_sum = sum(given_list)

    return actual_sum - given_sum


arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 9])
miss_num = missing_num(arr)

if miss_num > 0:
    print('Missing number', missing_num(arr))
else:
    print('No missing no. found')