num_of_nos = int(input("Enter number of numbers: "))

# psum = 0
# nsum = 0
count = 0
max = int(input("Enter a number:"))
while count < num_of_nos - 1:
    n = int(input("Enter a number:"))
    if n > max:
        max = n

    # if n > 0:
    #     psum = psum + n
    # else:
    #     nsum = nsum + n
    count = count + 1

# print('Positive Sum is', psum)
#
# print('Negative Sum is', nsum)
print('Max num is', max)
