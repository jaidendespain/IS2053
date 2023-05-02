# Global Variables.
GRAVITY = 9.8

def fallingDistance(t):
    distance_traveled_per_second = 0.5 * GRAVITY * t **2
    print(distance_traveled_per_second)

def main():
    print("This program determines the distance an object has traveled while in a state of free fall.")
    
    print("How many seconds will your object be falling?")
    time_of_fall = float(input())

    seconds_passed = 0
    while time_of_fall >= 1:
        seconds_passed += 1
        time_of_fall -= 1
        fallingDistance(seconds_passed)
    
main()
