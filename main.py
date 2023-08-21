import random
import time

def generate_question():
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
num_questions = 5
  
for _ in range(num_questions):
        question, correct_answer = generate_question()
        print(question)