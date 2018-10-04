
my_name = "Fabian Mazurek"
my_age = 18
my_height = 170 #cm roughly
my_weight = 75 #Kg
my_eyes = "Green"
my_hair = "Dark Brown"
is_heavy = my_weight > 3000
inches = 2.54
cm = 0.393701

print(f"Let's talk about {my_name}.")
print(f"He is {my_height} cm tall.")
print(f"He's {my_weight} kg heavy.")
print(f"It is {is_heavy} that he is overweight.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

height = input("Enter your height in Inches:")
height_in_cm = float(height) * float(inches)
print(f"Your are {height} inches or {height_in_cm}cm tall")
system = input("Would you like to convert to cm or inches?:")
if system == "inches":
    height1 = input("Enter a value in inches:")
    print(float(height1) * float(inches))
else:
    height2 = input("Enter a value in cm:")
    print(float(height2) / float(inches))
