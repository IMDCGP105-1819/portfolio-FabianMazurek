user_name = input("Enter your full name:")
user_age = input("Enter your age:")
if int(user_age) <= int(17):
    print("You probably aren't that young")
if 17 < int(user_age) < 25:
    print("Student?")
if int(user_age) >= int(26):
    print("Lets not talk about it :)")
user_height = input("Enter your height in cm:")
if int(user_height) <= int(160):
    print("One short BOI")
if 161 < int(user_height) < 180:
    print("One average BOI")
if int(user_height) >= 181:
    print("One very tall BOI")
user_weight = input("Enter your weight in kg:")
if int(user_weight) <= 60:
    print("Maybe eat more MEAT? :)")
if 61 < int(user_weight) < 75:
    print("You are below average in weight")
if 76 < int(user_weight) < 90:
    print("One average BOI (in UK)")
if int(user_weight) >= 91:
    print("THICCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
user_eye_colour = input("Enter your eye colour:")
user_hair_colour = input("Enter your hair colour:")
print("THANKS FOR TAKING THIS NOT VERY ANONYMOUS SURVEY, ALL DATA WILL BE USED AGAINST YOU AT SOME POINT maybe.")
