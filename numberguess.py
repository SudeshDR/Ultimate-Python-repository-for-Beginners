logo=""" _   _ _    _ __  __ ____  ______ _____     _____ _    _ ______  _____ _____ _____ _   _  _____    _____          __  __ ______ 
 | \ | | |  | |  \/  |  _ \|  ____|  __ \   / ____| |  | |  ____|/ ____/ ____|_   _| \ | |/ ____|  / ____|   /\   |  \/  |  ____|
 |  \| | |  | | \  / | |_) | |__  | |__) | | |  __| |  | | |__  | (___| (___   | | |  \| | |  __  | |  __   /  \  | \  / | |__   
 | . ` | |  | | |\/| |  _ <|  __| |  _  /  | | |_ | |  | |  __|  \___ \\___ \  | | | . ` | | |_ | | | |_ | / /\ \ | |\/| |  __|  
 | |\  | |__| | |  | | |_) | |____| | \ \  | |__| | |__| | |____ ____) |___) |_| |_| |\  | |__| | | |__| |/ ____ \| |  | | |____ 
 |_| \_|\____/|_|  |_|____/|______|_|  \_\  \_____|\____/|______|_____/_____/|_____|_| \_|\_____|  \_____/_/    \_\_|  |_|______|
                                                                                                                                 
                                                                                                                                 """
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  #print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()

