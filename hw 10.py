# TO GET MARKS FROM USER AND PRINT IT ONE BY ONE AND FIND TOTAL AND PERCENTAGE

e = float(input("Enter english marks : "))
m = float(input("Enter maths marks : "))
p = float(input("Enter physics marks : "))
csc = float(input("Enter computer marks : "))
c = float(input("Enter chemistry marks : "))
l = float(input("Enter language marks : "))

print("\n =============================================================")

print("\n ENG = ",e)
print("\n MATHS = ",m)
print("\n PHYSICS = ",p)
print("\n COMPUTER = ",csc)
print("\n CHEMISTRY = ",c)
print("\n LANGUAGE = ",l)

print("\n =============================================================")

tot = e + m + p + csc + c + l
pr = (tot / 600) * 100

print("\n Total marks obtained : ", tot)
print("\n Total Percentage : ", pr)

print("\n =============================================================")