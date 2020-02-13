import math
def my_abs(x):
    if not isinstance(x,(float,int)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x
    
def move(x,y,step,angle = 0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny

def quadratic(a,b,c):
    if (b**2 - 4*a*c) < 0:
        raise NotImplementedError('the zero of function isn\'t exit ')
    x1 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    return x1,x2