import random


class MathGame:

    def __init__(self):
        self.mark = 0
        self.level = None

    def get_level(self):
        while True:
            print("""Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29""")
            try:
                answer = int(input())
            except ValueError:
                print("Incorrect format.")
            else:
                if int(answer) in (1, 2):
                    self.level = int(answer)
                    break
                else:
                    print("Incorrect format.")

    def simple_question(self):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operands = ["+", "-", "*"]
        op = random.choice(operands)
        result = None
        print(a, op, b)
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("Incorrect format.")
            else:
                if int(answer) == result:
                    print("Right!")
                    self.mark += 1
                else:
                    print("Wrong!")
                break

    def hard_question(self):
        a = random.randint(11, 29)
        result = a ** 2
        print(a)
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("Incorrect format.")
            else:
                if int(answer) == result:
                    print("Right!")
                    self.mark += 1
                else:
                    print("Wrong!")
                break

    def print_to_file(self):
        print("Would you like to save your result to the file? Enter yes or no.")
        user_input = input()
        if user_input == "y" or user_input == "yes" or user_input == "YES" or user_input == "Yes":
            print("What is your name?")
            user_input = input()
            file = open("results.txt", "a")
            if self.level == 1:
                file.write(f"{user_input}: {self.mark}/5 in level 1 (simple operations with numbers 2-9).\n")
            elif self.level == 2:
                file.write(f"{user_input}: {self.mark}/5 in level 2 (integral squares 11-29).\n")
            file.close()
            print('The results are saved in "results.txt".')

    def run_game(self):
        self.get_level()
        if self.level == 1:
            for _ in range(5):
                self.simple_question()
        elif self.level == 2:
            for _ in range(5):
                self.hard_question()
        print(f"Your mark is {self.mark}/5.")
        self.print_to_file()


game = MathGame()
game.run_game()
