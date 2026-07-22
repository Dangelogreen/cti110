# D'Angelo Green
# 7/21/2026
# P5LAB
# Self checkout change calculator

import random

def disperse_change(change):

    change = round(change * 100)

    dollars = change // 100
    change = change % 100

    quarters = change // 25
    change = change % 25

    dimes = change // 10
    change = change % 10

    nickels = change // 5
    change = change % 5

    pennies = change

    if dollars > 0:
        print(dollars, "Dollars")

    if quarters > 0:
        print(quarters, "Quarters")

    if dimes > 0:
        print(dimes, "Dimes")

    if nickels > 0:
        print(nickels, "Nickels")

    if pennies > 0:
        print(pennies, "Pennies")

    if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        print("No change")


def main():

    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${amount_owed:.2f}")

    cash = float(input("How much cash will you put in the self-checkout? "))

    change = cash - amount_owed

    print(f"Change is: ${change:.2f}")
    print()

    disperse_change(change)


main()