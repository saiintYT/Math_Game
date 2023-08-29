import random
import time
import os

def clear_console():
  # Nate Lepper
  # August 30 2023
  # Clears Console
  # Version 1
    # Clear console screen for Windows and Unix-like systems
    os.system('cls' if os.name == 'nt' else 'clear')

def starting_menu():
  # Nate Lepper
  # August 30 2023
  # Starting Menu
  # Version 3
  print("Welcome to the Math Game!")
  print("You will be presented with addition and subtraction questions.")
  print("You have 3 lives.")
  print("Good luck!\n")
  

def generate_question():
  # Nate Lepper
  # August 30 2023
  # Random Question Generate
  # Version 3
  num1 = random.randint(1, 50)
  num2 = random.randint(1, 50)
  operator = random.choice(['+', '-'])

  if operator == '-' and num1 < num2:
    num1, num2 = num2, num1  # Swap numbers to avoid negative results

  question = f"What is {num1} {operator} {num2}? "
  answer = num1 + num2 if operator == '+' else num1 - num2
  return question, answer


def main():
# Nate Lepper
# August 30 2023
# Main math game function
# Version 3
  score = 0
  # Set Score
  num_questions = 5
  # Set Number of Questions
  lives = 3
  # Main Sequence
  starting_menu()

  playing = True
  while playing:
  # player loop
  # Version 1
    for _ in range(num_questions):
      # Printing Number Generation on Console
      # Version 3
      question, correct_answer = generate_question()
      print(question)

      user_answer = input("Your answer: ")

      try:
        if int(user_answer) == correct_answer:
          print("Correct!\n")
          score += 1
        else:
          print(f"Wrong! The correct answer is {correct_answer}\n")
      except ValueError:
        print("Invalid input. Please enter a valid number.\n")

    print(f"Game over! Your score: {score}/{num_questions}")
    play_again_input = input("Do you want to play again? (yes/no): ")
    play_again = play_again_input.lower() == 'yes'

    if play_again:
      print("\nStarting a new game...\n")
      clear_console()
      starting_menu()
      score = 0
      lives = 3
    else:
      print("Thank you for playing!")
      playing = False


if __name__ == "__main__":
  main()
