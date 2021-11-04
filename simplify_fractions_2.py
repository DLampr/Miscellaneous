"""Another try of the simplify fractions program"""

a = int(input("Give me the numerator value: "))
b = int(input("Give me the denominator value: "))

def prog(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
    
print("Greatest common divisor: "+ str(prog(a, b)))

number_up = int(a / prog(a, b))
number_down = int(b / prog(a, b))

print(str(number_up)+"/"+str(number_down))
