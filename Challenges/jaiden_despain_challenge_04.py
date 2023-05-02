 # Variables
answer = int(41) # Correct Guess.
num_guesses = int(0) # Number of Guesses.
user_guess = int(0)
game_running = True

 # Starting the game.
user_response = input("Wanna play a guessing game? (yes/no) \n")

# User responds 'yes'
if (user_response.lower() == "yes"):
    print("Guess a number between 1 and 50.")
    while game_running == True:

        # Input validation.
        try:
            user_guess = int(input())
        except ValueError:
            print("Please enter a number between 1 and 50.")
            continue

        num_guesses += 1
        # Guess between 1 and 50.
        if 1 <= user_guess <= 50:

            # Correct Guess.
            if user_guess == answer:
                print("Congratulations. You guessed the correct number.")

                # Printing number of guesses.
                if num_guesses == 1:
                    print("It took you " + str(num_guesses) + " guess to find the answer.")
                elif num_guesses > 1:
                    print("It took you " + str(num_guesses) + " guesses to find the answer.")
                game_running = False

            # Within-5 guess.
            elif user_guess >= answer - 5 and user_guess <= answer + 5 and user_guess != answer:
                print("Your guess is within 5 digits of the correct number. Please try again.")
            
            # Wrong guess.
            else:
                print("That is not the correct number. Please try again.")

        # Guess outside 1 and 50.
        if user_guess > 50 or user_guess < 1:
            print("Please enter a number between 1 and 50.")

# User responds 'no'
else:
    print("Well, goodbye!")
