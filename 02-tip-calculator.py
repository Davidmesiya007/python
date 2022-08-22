# Tip Calculator
print("Welcome to the tip caluclator")
total_bill = float(input("what was the total bill"))
bill_per = int(input("what percentage tip would you want to give ? 10 12 15\n"))
tip = float((total_bill/100)*bill_per)
bill = total_bill+tip
# here n is how many people share the bill amount
n = int(input("how many members share the bill amount? "))
split_bill = bill/n
# print(round(split_bill, 2))
final_bill_amount = round(split_bill,2)
final_bill_amount = "{:.2f}".format(split_bill)
print(final_bill_amount)




