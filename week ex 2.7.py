word = input("enter a word: ")
number = int(input("enter a number: "))
for i in range(len(word)):
    temp = 0
    while temp < number:
        print(word[i], end = "")
        temp += 1
