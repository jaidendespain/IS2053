# Checking the entered number.
def check_num(n):
    if len(n) != 12:
        return False
    
    if n[3] and n[7] != "-":
        return False
    
    numbers = n[0:3] + n[4:7] + n[8:13]
    if not numbers.isnumeric():
        return False
    
    return True


# User interface.
def menu():
    while True:
        user_input = input("\nEnter a phone number (Ex '555-935-5342'): ")
        
        if check_num(user_input) == True:
            print(f"{check_num(user_input)}. '{user_input}' is a valid phone number.")
            break
        elif check_num(user_input) == False:
            print(f"{check_num(user_input)}. '{user_input}' is not valid phone number.")


# Main function.
def main():
    menu()


if __name__ == "__main__":
    main()
