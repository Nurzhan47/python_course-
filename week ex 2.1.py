import math
print("Smart Calculator")
first = int(input("First number: "))
second = int(input("Second number: "))
operation = input("Operation: ")


if operation == "+":
    print("%2d + %2d = %2d" % (first,second,first+second))
if operation == "-":
    print("%2d - %2d = %2d" % (first,second,first-second))
if operation == "*":
    print("%2d * %2d = %2d" % (first,second,first*second))
if operation == "/":
    if second == 0:
        print("can not divide by 0")
    else:
        print("%2d / %2d = %2d" % (first,second,first/second))
