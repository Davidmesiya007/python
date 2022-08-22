import random
names = input("Enter the names : ")
split_names = names.split(",")
names_length = len(split_names)
random_choice = random.randint(0, names_length-1)
person = split_names[random_choice]
print(f"{person} will pay the fees")