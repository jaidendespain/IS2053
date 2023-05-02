# Checking the user's password against common passwords.
def stored_passwords(password):
    stored_passwords = str(('123456', '123456789', '12345', 'qwerty', 'password', '12345678', '111111', '123123', '1234567890', '1234567', 'qwerty123', '000000', '1q2w3e', 'aa12345678', 'abc123', 'password1', '1234', 'qwertyuiop', '123321', 'password123', '1q2w3e4r5t', 'iloveyou', '654321', '666666', '987654321', '123', '123456a', 'qwe123', '1q2w3e4r', '7777777', '1qaz2wsx', '123qwe', 'zxcvbnm', '121212', 'asdasd', 'a123456', '555555', 'dragon', '112233', '123123123', 'monkey', '11111111', 'qazwsx', '159753', 'asdfghjkl', '222222', '1234qwer', 'qwerty1', '123654', '123abc'))

    # Outputing the password's index, if there is one.
    if password in stored_passwords:
        print(f"Your password is too common. Please consider changing it. '{password}' was found at index {stored_passwords.index(password)}")

    else:
        print("You have a strong password.")

# Getting the user's name and password.
def get_user_password():
    user_name = input("Please enter a username: ")
    user_password = input("Please enter a password: ")

    # Outputting the user's name and whether or not the entered password is common.
    print(user_name, end = ". ")
    stored_passwords(user_password)

# Main
def main():
    get_user_password()

main()
