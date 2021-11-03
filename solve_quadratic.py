"""A function, that returns both solutions of a generic quadratic as a pair (2-tuple) 
   when the coefficients are given as parameters"""

import math
 
def solve_quadratic(a, b, c):
    x = (-b+math.sqrt((b)**2-(4*a*c)))/(2*a)
    y = (-b-math.sqrt((b)**2-(4*a*c)))/(2*a)
    return x,y
 
def main():
    pass
 
if __name__ == "__main__":
    main()
