# Ask the user for their name.
# Print this exact message to the console:  “Hello [the user's name will go here].  Welcome to the Python Pizza chooser.”
# Print another statement with three types of pizzas the user can choose exactly like this:  "Would you like to order a cheese pizza, a pepperoni pizza, or a supreme pizza?"
# Using a Decision Structure(s), allow the user to choose which pizza(s) they wish to buy.
# Using Input Validation, ensure the user actually types cheese, pepperoni or supreme.  For instance, Mushroom pizza should not be allowed. 
# Print this exact statement if the user enteres anything not allowed:  "You may choose to order a cheese, pepperoni, or supreme pizza only.  Please choose again." 
# Using a Repetition Structure, continue to ask the user if they want to order another pizza until they answer: “no”.  You will need to deal with case here, so force their input into either lower or upper case. 
# Once the user has chosen to finalize their order, print the following statement:   “Thank you [insert name here].  The [insert number of pizzas here] pizzas you ordered will be ready in 30 minutes.”

# Greeting the user.
user_name = input("Hello, what's your name? \n")
print(f"Hello {user_name}. Welcome to Python Pizza chooser.")

# Pizza time.
program_running = True
num_pizzas = 0
while program_running == True:
    pizza_choice = input("Would you like to order a cheese pizza, a pepperoni pizza, or a supreme pizza? \n")

    # Input validation.
    while program_running == True:
        if pizza_choice.lower() == "cheese" or pizza_choice.lower() == "pepperoni" or pizza_choice.lower() == "supreme":
            num_pizzas += 1
            break
        elif pizza_choice.lower() == "no":
            program_running = False
            break
        else:
            print("You may choose to order a cheese, pepperoni, or supreme pizza only. Please choose again.")
            pizza_choice = input()
            continue

    # Continue ordering?
    while program_running == True:
        while num_pizzas >= 1:
            ordering = input("Would you like to order another pizza? \n")
            if ordering.lower() == "no":
                program_running = False
                break
            elif ordering.lower() == "yes":
                break
            else:
                continue
        break

# End of transaction.
print(f"Thank you {user_name}. The {num_pizzas} pizzas you ordered will be ready in 30 minutes.")
