 # Green Dangelo    
 # 06/20/2026
 # p1hw2
 # create a program that does some basic math on numbers that are entered


# Green Dangelo
# 06/20/2026
# P1HW2_GreenDangelo
# Python program that calculates travel expenses

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
print()

destination = input("Enter your travel destination: ")
print()

gas = int(input("How much do you think you will spend on gas? "))
print()

hotel = int(input("Approximately, how much will you need for accommodation/hotel? "))
print()

food = int(input("Last, how much do you need for food? "))
print()

# math
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

print("-----------Travel Expenses-----------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", hotel)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)
