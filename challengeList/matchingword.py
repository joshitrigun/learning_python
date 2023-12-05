words =['pizza', 'burger', 'momo', 'chowmein', 'thuppa', 'pasta']


userinput = input('Enter a letter: ')

for i in words:
    # if i[0] == userinput:
    #     print(i)
    if i.startswith(userinput):
        print(i)