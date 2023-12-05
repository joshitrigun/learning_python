userInput = int(input("Enter a number to determine if its palindrome or not?"))
n = userInput

# count = 0
sum = 0
reverse = 0
while n > 0:
    rem = n % 10
    # sum += rem
    n = n // 10
    reverse = reverse * 10 + rem

    # count += 1
# print("count", count)
# print("sum", sum)
# print("rev", reverse)

if userInput == reverse:
    print("palindrome")
else:
    print("not palindrome")