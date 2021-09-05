# TO FIND THE AREA OF TRIANGLE WITH HERONS FORMULA

import math

a = float(input("Enter value for a : "))
b = float(input("Enter value for b : "))
c = float(input("Enter value for c : "))

s = (a + b + c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("\n The area of triangle is =", area)