import random
import time


def starting_menu():
  print("Welcome to the Math Game!")
  print("You will be presented with addition and subtraction questions.")
  print("You have 3 lives.")
  print("Good luck!\n")


def generate_question():
  num1 = random.randint(1, 50)
  num2 = random.randint(1, 50)
  operator = random.choice(['+', '-'])

  if operator == '-' and num1 < num2:
    num1, num2 = num2, num1  # Swap numbers to avoid negative results

  question = f"What is {num1} {operator} {num2}? "
  answer = num1 + num2 if operator == '+' else num1 - num2
  return question, answer


def main():
  score = 0
  num_questions = 5
  lives = 3

  starting_menu()

  playing = True
  while playing:
    for _ in range(num_questions):
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
      score = 0
      lives = 3
    else:
      print("Thank you for playing!")
      playing = False


if __name__ == "__main__":
  main()
