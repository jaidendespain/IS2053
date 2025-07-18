# Checking the user's password against common passwords.
def password_check(entered_password):
    stored_passwords = ['123456', '123456789', '12345', 'qwerty', 'password', '12345678', '111111', '123123', '1234567890', '1234567', 'qwerty123', '000000', '1q2w3e', 'aa12345678', 'abc123', 'password1', '1234', 'qwertyuiop', '123321', 'password123', '1q2w3e4r5t', 'iloveyou', '654321', '666666', '987654321', '123', '123456a', 'qwe123', '1q2w3e4r', '7777777', '1qaz2wsx', '123qwe', 'zxcvbnm', '121212', 'asdasd', 'a123456', '555555', 'dragon', '112233', '123123123', 'monkey', '11111111', 'qazwsx', '159753', 'asdfghjkl', '222222', '1234qwer', 'qwerty1', '123654', '123abc']
    stored_passwords.append(entered_password)

    # Password checks
    unique = True
    capital = False
    lowercase = False
    number = False
    special = False
    length = False
    
    # Seperating the user's password into a list.
    password = []
    for element in entered_password:
        password.append(element)

    # Checking the password's strength.
    if any(element.isupper() for element in password):
        capital = True

    #lowercase check.
    if any(element.islower() for element in password):
        lowercase = True

    # Number check
    if any(element.isdigit() for element in password):
        number = True

    # Special character check.
    for element in password:
        if (element=='!' or element=='@' or element=='%' or element=='^' or element=='&' or element=='*' or element=='(' or element==')'):
            special = True

    # Minimum lenghth check.
    if len(password) >= 8:
        length = True

    # Printing the results.
    if unique == True and capital == True and lowercase == True and number == True and special == True and length == True:
        print('You have a strong password.')

    else:
        print('Please enter another password containing at least one capital letter, one lowercase letter, \none number, one special character, and is at least 8 characters long.')

# Getting the user's name and password.
def get_user_password():
    user_name = input("Please enter a username: ")
    user_password = input("Please enter a password: ")

    # Outputting the user's name and whether or not the entered password is common.
    print(user_name, end = ". ")
    password_check(user_password)

# Main
def main():
    get_user_password()

main()
