"""A program that can compute the areas of three shapes, triangles, rectangles and circles, when their dimensions are given.
   An endless loop asks for which shape you want the area be calculated.
   An empty string as input will exit the loop.
   If the user gives a string that is none of the given shapes, the message “Unknown shape!” will be printed.
   Then it will ask for dimensions for that particular shape.
   When all the necessary dimensions are given, it prints the area, and starts the loop all over again."""

import math 
 
def main():
 
    def rectangle(w,h):
        """Calculates the area of a rectangle"""
        return w*h
    
    def circle(r):
        """Calculates the area of a circle"""
        return (r**2)*math.pi
    
    def triangle(b,h):
        """Calculates the area of a triangle"""
        return (b*h)/2
 
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == '':
            break
        elif shape == 'triangle':
            b = float(input("Give base of the triangle: "))
            h = float(input("Give height of the triangle: "))
            print(f"The area is {triangle(b,h)}")
        elif shape == 'rectangle':
            w = float(input("Give width of the rectangle: "))
            h = float(input("Give height of the rectangle: "))
            print(f"The area is {rectangle(w,h)}")
        elif shape == 'circle':
            r = float(input("Give radius of the circle: "))
            print(f"The area is {circle(r)}")
        else:
            print("Unknown shape!")
            
if __name__ == "__main__":
    main()

