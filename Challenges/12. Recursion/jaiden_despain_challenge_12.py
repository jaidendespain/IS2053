# Finding the factorial.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Finding the factorial multiples.
def factorial_multiples(n):
    if n == 0:
        return []
    else:
        multiples = [n] + factorial_multiples(n - 1)
        return multiples


# Determining if num is prime.
def find_prime(n, i=2):
    if n < 2:
        return False
    elif i == n:
        return True
    elif n % i == 0:
        return False
    else:
        return find_prime(n, i+1)


# UI.
def menu():
    # Asking the user to enter a number.
    while True:
        try:
            num = int(input("Enter a number: "))
            if num < 0:
                print("Your number MUST be positive.")
            else:
                break
        except ValueError:
            print("Please enter a whole number.")
    
    # Asking the user to choose factorial or prime.
    valid_functions = ["factorial", "prime"]
    function = input(f"Would you like to find the factorial or determine if it's a prime number?: ")
    while function.lower() not in valid_functions:
        function = input("Enter 'prime' or 'factorial': ")

    # Calling the factorial function.
    if function == "factorial":
        result = factorial(num)
        multiple_num = factorial_multiples(num)
        multiples = "({})".format(" * ".join(str(num) for num in multiple_num))
        print(f"\nThe factorial of {num} is {result}.")
        print(multiples)
    
    # Calling the prime function.
    elif function == "prime":
        result = find_prime(num)
        if result == True:
            print(f"{num} is a prime number.")
        elif result == False:
            print(f"{num} is not a prime number.")


# Main function.
def main():
    menu()


if __name__ =="__main__":
    main()
