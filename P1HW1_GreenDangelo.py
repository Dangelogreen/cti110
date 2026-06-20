# Green Dangelo
# 06/20/2026
# p1hw1
# Python program that uses mathematical expressions

print("----Calculating Exponents----")
print()

base = int(input("Enter an integer as the base number:  "))
exponent = int(input("Enter an integer as the exponent:  "))
print()
print()

result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, "!!")
print()
print()

#calculate addistion and subtraction
print("----Addition and Subtraction----")
print()

num1 = int(input("Enter a starting integer:"))
num2 = int(input("Enter an integer to add:"))
num3 = int(input("Enter an integer to subtract:"))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result, "!!")