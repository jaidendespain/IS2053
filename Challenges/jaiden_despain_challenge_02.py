# Asking for the user's name.
print("What's your name?")
user_name = str(input())

# Asking for the user's birth year.
print("Hey " + user_name + ", what year were you born? " + "(yyyy)")
user_birthyear = int(input())

# Determining the user's age. I calculate use -1 for a better approximation.
user_age = (2023 - user_birthyear) - 1
print("Your name is " + user_name + ". " + "You were born in " + str(user_birthyear) + ". " + "That makes you approximately " + str(user_age) +" years old.")
