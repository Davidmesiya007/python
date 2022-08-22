#Welcome to my Body Mass Index Caluculator version 2.0
print("Welcome to my BMI calculator")
height = float(input("Enter your height in m  : "))
weight = float(input("Enter your weight in kg : "))
bmi = round(float((weight/(height**2))), 2)
# bmi = "{:.2f}".format{bmi)
print(f"your bmi is = {bmi}")
if bmi < 18.5:
  print("Under weight")
elif bmi <25:
  print("Normal")
elif bmi < 30:
  print("overweight")
elif bmi < 35:
  print("Obase")
else:
  print("Clinically Obase")