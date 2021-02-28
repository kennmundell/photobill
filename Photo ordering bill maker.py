# to calculate a bill for photos
print()
print("Welcome to my photo cost calculator")
print()
six_by_four = float(input("Please input price for each 6x4 print in £'s "))
seven_by_five = float(input("Input price for 7x5 prints in £'s "))
a4 = float(input("Please input price for a4 prints in £'s "))

# input how many prints bought
print()
print("Now enter how many prints bought")
print()

six_four_orders = int(input("How many 6x4's bought "))
seven_five_orders = int(input("How many 7x5's bought "))
a4_orders = int(input("How many a4's bought "))

six_total = six_four_orders * six_by_four
seven_total = seven_five_orders * seven_by_five
a4_total = a4_orders * a4
total_bill = six_total + seven_total + a4_total
#total_bill_dec = ("{:.2f)".format(total_bill))
print()

print(f"Your total bill is £" + "{:.2f}".format(total_bill))
