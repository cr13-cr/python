#FIBONACCI SERIES

n = int(input("Enter the value of 'n': "))
a = -1
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = "\t")
while(count <= n):
  print(sum, end = "\t")
  count += 1
  a = b
  b = sum
  sum = a + b