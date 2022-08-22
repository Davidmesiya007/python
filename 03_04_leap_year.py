#Leap year calculation
print("welcome to leap year identifier")
year = int(input("Enter the year : "))
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print("Leap year")
    else:
      print("not a leap year")
  else: 
    print("leap year") 
else:
  print("not leap year")
  
