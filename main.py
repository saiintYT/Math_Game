import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def introduction():
    print("Welcome to the Math Game!")
    print("In this game, you will be presented with addition and subtraction questions.")
    print("Your goal is to answer as many questions correctly as possible.")
    print("You will start with 3 lives. Each wrong answer will cost you a life.")
    print("The game will end when you run out of lives or after 5 questions.")
    print("Good luck!\n")

def get_player_name():
    name = input("Please enter your name: ")
    return name

def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-'])

    if operator == '-' and num1 < num2:
        num1, num2 = num2, num1

    question = f"What is {num1} {operator} {num2}? "
    answer = num1 + num2 if operator == '+' else num1 - num2
    return question, answer

def load_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard = [line.strip().split(",") for line in file]
    except FileNotFoundError:
        leaderboard = []
    return leaderboard

def save_leaderboard(leaderboard):
    with open("leaderboard.txt", "w") as file:
        for entry in leaderboard:
            file.write(",".join(entry) + "\n")

def display_leaderboard(leaderboard):
    print("\nLeaderboard:")
    if leaderboard:
        leaderboard.sort(key=lambda x: int(x[1]), reverse=True)
        max_name_length = max(len(entry[0]) for entry in leaderboard)
        max_score_length = len(max(leaderboard, key=lambda x: len(x[1]))[1])
        for rank, (name, score) in enumerate(leaderboard, start=1):
            padding = max_name_length + max_score_length + 8 - len(name) - len(score)
            print(f"{rank}. {name}:{' ' * padding}{score}")
    else:
        print("The leaderboard is empty.")

def main():
    introduction()
    player_name = get_player_name()
    print(f"Hello, {player_name}!\n")

    leaderboard = load_leaderboard()

    while True:
        score = 0
        num_questions = 5
        lives = 3

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
                        lives -= 1
                        if lives == 0:
                            print("Out of lives. Game over!")
                            playing = False
                            break
                except ValueError:
                    print("Invalid input. Please enter a valid number.\n")

            if lives > 0:
                print(f"Game over, {player_name}! Your score: {score}/{num_questions}")
                leaderboard.append((player_name, str(score)))
                save_leaderboard(leaderboard)
                display_leaderboard(leaderboard)

                play_again_input = input("Do you want to play again? (yes/no): ")
                if play_again_input.lower() == 'no':
                    print(f"Thank you for playing, {player_name}!")
                    playing = False
                elif play_again_input.lower() != 'yes':
                    print("Please enter 'yes' or 'no'.")
                else:
                    print("\nStarting a new game...\n")
                    clear_console()
            else:
                print(f"Game over, {player_name}! Your score: {score}/{num_questions}")
                print("You have run out of lives. Better luck next time!")
                leaderboard.append((player_name, str(score)))
                save_leaderboard(leaderboard)
                display_leaderboard(leaderboard)

if __name__ == "__main__":
    main()
