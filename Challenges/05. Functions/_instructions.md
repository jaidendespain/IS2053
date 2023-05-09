# Instructions

The program will determine the distance an object has traveled while in free fall. This will be done by using the falling distance formula, variables and constants, and two functions. The program will accept the time of fall from the user, then calculate and print the distance traveled at each second.

Formula for Falling Distance:
Free-falling objects are in a state of acceleration. They are accelerating at a rate of 9.8 m/s^2. The velocity of a free-falling object changes by 9.8 m/s every second. Thus, the velocity of a free-falling object that has been dropped from rest is dependent on the time it has fallen. The formula for determining the distance an object falls after a time of t seconds is: **d = 0.5 * g * t^2** where g = 9.8 m/s^2 (gravity), t = time, and d = distance.

Program Instructions:

1. Create two functions: main() and fallingDistance()
2. Inside the main() function, greet the user and explain what the program does.
3. Ask the user to enter the time of fall (in seconds) for the object.
4. Pass the value of time_of_fall (declared in main) to the fallingDistance() function.
5. Inside the fallingDistance() function, calculate the distance at each moment in time using the falling distance formula.
6. Print the distance traveled at each second using the print() function.


Note: The program will calculate and print the distance traveled at every second, not just the end.