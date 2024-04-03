import random

def guess_number():
    number_to_guess =random.randint(1,100)
    attempts = 0
    
    print("Welcom to  the number guessing Game!")
    print("1've chosen a number between 1 and 100.Try to guess it.")
    while True:
        guess = int(input("enter your guess:"))
        attempts +=1
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number{number_to_guess} in {attempts}attempts.")
        break
guess_number()
                      