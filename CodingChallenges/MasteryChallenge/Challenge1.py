import random

def main():
    print("Welcome to the Number Guessing Game!")
    random_integer = random.randint(1, 101)
    user_guess = int(input("Guess a number between 1 and 100: "))
    while(user_guess != random_integer):
        if user_guess < random_integer:
            print("Too low!")
        elif user_guess > random_integer:
            print("Too high!")
        user_guess = int(input("Guess again: "))
    print("Congratulations! You guessed the number.")

if __name__ == "__main__":
    main()
