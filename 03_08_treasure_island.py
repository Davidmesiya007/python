print(
  '''
  
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to my treasure Island")
print("Your mission is find a treasure")
choice1 = input("you're at a cross a road. where do you want to go?type left or right : ")
choice1_lower = choice1.lower()
if choice1_lower == "left":
  #continue the game
  choice2 = input("Two choices are there  wait for boat or swim the lake to cross? type 'wait' or 'swim' : ")
  choice2_lower = choice2.lower()
  if choice2_lower == "wait":
    choice3= input("There are three doors available colores are 'red','blue' and 'yellow' choose any color : ")
    choice3_lower = choice3.lower()
    if choice3_lower == "yellow":
      print("you won the game. you pass through lot of interruption and finally you reached the treasure.")
    elif choice3_lower == "red":
      print("room full of fire. So game over")
    else:
      print("room full of water. so game over")
  else:
    print("you attack by crocodile. So game over")
else:
  print("you fell in to a hole. So game over.")
