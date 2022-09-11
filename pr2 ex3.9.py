import math
x=int(input())
y=int(input())
z=int(input())
b=3*x
a=(math.log1p((x-3)**4)+2*math.sin(b)*math.sin(b))/(4*x-5.2)
print('%.2f' % a)
