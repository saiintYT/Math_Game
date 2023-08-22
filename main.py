import random
import time

def starting_menu():

  # Nate Lepper
  # August 22 2023
  # Starting Menu
  # Version 1
  
    print("Welcome to the Math Game!")
    print("You will be presented with addition and subtraction questions.")
  
def generate_question():
  # Nate Lepper
  # August 21 2023
  # Random Question Generate
  # Version 1
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-'])
    if operator == '-':
        if num1 < num2:
            num1, num2 = num2, num1  # Swap numbers to avoid negative results
    question = f"What is {num1} {operator} {num2}? "
    answer = num1 + num2 if operator == '+' else num1 - num2
    return question, answer

score = 0
# Set Score
num_questions = 5
# Set Number of Questions

  # Main Sequence
starting_menu()
for _ in range(num_questions):
  # Nate Lepper
  # August 21 2023
  # Printing Number Generation on Console
  # Version 2
  question, correct_answer = generate_question()
  print(question)
  
  user_answer = input("Your answer: ")

  try:
  # Nate Lepper
  # August 22 2023
  # Getting User Input and Checking User Input
  # Version 2
      if int(user_answer) == correct_answer:
          print("Correct!\n")
          score += 1
      else:
          print(f"Wrong! The correct answer is {correct_answer}\n")
  except ValueError:
      print("Invalid input. Please enter a valid number.\n")

print(f"Game over! Your score: {score}/{num_questions}")