from tkinter import Y


print("welcome to my roller coaster")
height = int(input("Enter your height in cm : "))
bill = 0
if height > 120:
  age = int(input("Ener your age in year : "))
  if age < 12:
    bill = 5
    print("childrens tickets is $5")
  elif age <= 18:
    bill = 7
    print("youths tickets is $7")
  elif (age >= 45) and (age <=55):
    print("you travel free in roller coaster")
  else:
    bill = 12
    print("Adults tickets  $12")
  photo = input("Do you want a photo? Y or N ")
  if photo == "Y":
    bill = bill+3
  print(f"The total bill is = {bill}")
  # else:
  #   print(f"The total bill is = {bill}")
else:
  print("you are not eligible for rollercoaster") 