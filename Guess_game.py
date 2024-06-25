import random

def guess_game():
    num_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None
    
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Can you guess what it is?")
    
    while guess != num_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < num_to_guess:
                print("Too Low! Try again.")
            elif guess > num_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulation! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
if __name__ == "__main__":
    guess_game()