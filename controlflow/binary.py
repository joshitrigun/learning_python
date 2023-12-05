userInput = int(input("Enter a number: "))

binayNum = ''
rem = 0

while userInput > 0:
    rem = userInput % 2
    userInput = userInput // 2
    binayNum = str(rem) + binayNum



print('binary num', binayNum)
