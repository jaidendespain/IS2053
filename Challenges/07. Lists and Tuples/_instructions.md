# Instructions

In this programming challenge, you will write a program that checks if a user's password is too common. Here are the step-by-step instructions:


1. Create a function named StoredPasswords(checkPass) that takes in a password and returns a boolean value indicating whether or not the password is in a tuple containing the 50 most common passwords.
2. Create a function named getUserPass() that prompts the user to create a username and password and returns them as separate variables.
3. Create a function named main() or if '__name__=='__main__':'
4. In main(), call getUserPass() to prompt the user for their username and password.
5. In getUserPass(), call StoredPasswords(checkPass) with the user's password as an argument.
6. In StoredPasswords(checkPass), create a tuple containing the 50 most common passwords listed below.
7. Use a loop and the in operator to check if the user's password is in the tuple.
8. If the user's password is in the tuple, print "Your password is too common. Please consider changing it." Otherwise, print "You have a strong password."
9. Print the location in the tuple where the password was found (if it was found) inside StoredPasswords(checkPass) using the index() method of tuples.


Password List:
123456, 123456789, 12345, qwerty, password, 12345678, 111111, 123123, 1234567890, 1234567, qwerty123, 000000, 1q2w3e, aa12345678, abc123, password1, 1234, qwertyuiop, 123321, password123, 1q2w3e4r5t, iloveyou, 654321, 666666, 987654321, 123, 123456a, qwe123, 1q2w3e4r, 7777777, 1qaz2wsx, 123qwe, zxcvbnm, 121212, asdasd, a123456, 555555, dragon, 112233, 123123123, monkey, 11111111, qazwsx, 159753, asdfghjkl, 222222, 1234qwer, qwerty1, 123654, 123abc