import math


elps = math.exp(-10)

def func(x):
    return math.exp(x) - (x+2)

def main():
    a = 0 
    b = 2.0
    while abs(b-a)>elps :
        c = (a+b)/2
        if func(a)*func(c)<0 :
            b = c
        else:
            a = c
    return c
print(main())


