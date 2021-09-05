#TO CHECK WHETHER THE ENTERED CHARACTER IS VOWEL OR NOT

ch = input("Enter a character: ")

if ch in('a','A','e','E','i','I','o','O','u','U'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a not a vowel")