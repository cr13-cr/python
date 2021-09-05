#TO FIND THE SMALLEST OF THREE NUMBERS

a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

n = 0

if a < b and a < c :
    n = a
elif b < c :
    n = b
else :
    n = c

print(n, "is the smallest of three numbers.")