# Correct Answer / Number to guess.
answer = int(30)

# Starting the game.
print("Wanna play a guessing game?" + " " + "(yes/no)")
user_response = input()

# User responds 'yes'
if user_response == "yes" or user_response == "Yes" or user_response == "YES":
     
     # Number guessing.
     print("Guess a number between 1 and 50.")
     user_guess = int(input())

     # Correct guess.
     if user_guess == answer:
        print("Congratulations. You guessed the correct number.")

     # Within-5 guess.
     elif user_guess >= answer - 5 and user_guess <= answer + 5 and user_guess != answer:
        print("You were within 5 numbers of the correct value.")
    
     # Wrong guess.
     else:
        print("That is not the correct number.")


# User responds 'no'
else:
    print("Well, goodbye!")

