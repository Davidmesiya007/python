#You've got a job at python pizza, your first is to build on automatic pizza order program.
#based  on user's order work out their final bill
          # small pizza  : $15
          # Medium pizza : $20
          # Large pizza  : $25
          # Perpporponi for small pizza          : $2
          # pepperponi for medium or large pizza : $3
          # extra cheese for any pizza           : $1
from re import L, S
from tkinter import Y


print("welcome to my pizza delivaries")
pizza_size = input("what size pizza do you want? S M L")
add_pepporponi = input("Do you want pepporponi? Y or N ")
add_cheese = input("Do you want cheese? Y or N ")
prize = 0
if pizza_size == "S":
  print("nice! you choose small pizza")
  prize = 15
  if add_pepporponi == "Y":
    prize += 2
  if add_cheese == "Y":
    prize += 1
    print("")
  print(f"your pizza prize is = {prize}")
elif pizza_size == "M":
  print("nice! you choose medium pizza")
  prize = 20
  if add_pepporponi == "Y":
    prize += 3
  if add_cheese == "Y":
    prize += 1
  print(f"your pizaa prize is = {prize}")
elif pizza_size == "L":
  print("nice! you choose large pizza")
  prize = 25
  if add_pepporponi == "Y":
    prize += 3
  if add_cheese == "Y":
    prize += 1
  print(f"your pizaa prize is = {prize}")
else:
  print("wrong choice")