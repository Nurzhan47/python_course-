import math
x=float(input())
y=float(input())
z=float(input())
a=4*y
b=4*x
s=(math.asin(x)*math.asin(x)*math.asin(x)-6)/(8*(math.cos(a)-math.sin(b)))
print('%.2f' % s)
