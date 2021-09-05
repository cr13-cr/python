#TO CHECK WHETHER THE NUMBER IS PALINDROME OR NOT

n = int(input("Enter any number to check"))

m = n #The variable m is used to store the initial value of n

rev = 0

while(n>0):
    c = n % 10
    rev = rev * 10 + c
    n = n // 10
    
if(m == rev):
    print("The number is Palindrome")
else:
    print("The number is not Palindrome")