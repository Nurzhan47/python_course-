import math  
a = float(input('a: '))  
b = float(input('b: '))  
c = float(input('c: '))  
dis = (b**2) - (4*a*c)  
sol1 = (-b-math.sqrt(dis))/(2*a)  
sol2 = (-b+math.sqrt(dis))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2)) 
