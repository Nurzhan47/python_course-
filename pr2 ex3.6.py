import math
x=float(input())
y=float(input())
z=float(input())

a=(4*math.fabs(x)-x*y*(z**2))/(x+math.e**(y*x)-2*y*z)
print('%.2f' % a)
