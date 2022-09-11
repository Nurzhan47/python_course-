import math
a = float(input("A: "))
integer_part = math.trunc(a)
fractional_part = math.trunc((a * 100) % 100)
print(integer_part / 100 + fractional_part)
print("")
