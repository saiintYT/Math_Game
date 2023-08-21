import random
import time

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

for _ in range(num_questions):
  # Nate Lepper
  # August 21 2023
  # Printing Number Generation on Console
  # Version 1
        question, correct_answer = generate_question()
        print(question)