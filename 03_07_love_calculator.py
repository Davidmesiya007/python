# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
t1 = lower_name1.count('t')
r1 = lower_name1.count('r')
u1 = lower_name1.count('u')
e1 = lower_name1.count('e')
l1 = lower_name1.count('l')
o1 = lower_name1.count('o')
v1 = lower_name1.count('v')
t2 = lower_name2.count('t')
r2 = lower_name2.count('r')
u2 = lower_name2.count('u')
e2 = lower_name2.count('e')
l2 = lower_name2.count('l')
o2 = lower_name2.count('o')
v2 = lower_name2.count('v')
tot_left = t1+r1+u1+e1+t2+r2+u2+e2
tot_right = l1+l2+o1+o2+v1+v2+e1+e2
tot = int(f"{tot_left}{tot_right}")
if tot < 10 or tot > 90:
    print(f"Your score is {tot}, you go together like coke and mentos.")
elif tot > 40 and tot < 50:
    print(f"Your score is {tot}, you are alright together.")
else:
    print(f"Your score is {tot}.")



