''' TO FIND GROSS SALARY BY GETTING BASIC SALARY AS INPUT FROM USER 

    BASIC SALARY < 25000 : HRA = 20% ; DA = 80%
    BASIC SALARY >= 25000 : HRA = 25% ; DA = 90%
    BASIC SALARY >= 40000 : HRA = 30% ; DA = 95%'''

basic = float(input("Enter Basic Salary Of Employee"))

if(basic<25000):
    da = basic * 80 / 100
    hra = basic * 20 / 100
elif(basic>=25000 or basic<40000):
    da = basic * 90 / 100
    hra = basic * 25 / 100
elif(basic>=40000):
    da = basic * 95 / 100
    hra = basic * 30 / 100

gross = basic + hra + da

print("\n\t Basic Pay : ", basic)
print("\n\t Dearness Allowance : ", da)
print("\n\t House Rent Allowance : ", hra)
print("\n\t-------------------------------------------")
print("\n\t Gross Salary : ", gross)
print("\n\t-------------------------------------------")