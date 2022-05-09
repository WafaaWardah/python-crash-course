# This is a simple Arithmetic quiz
# Python concepts: variables, data types, user input, if...else decision,
# loop, random, functions, simple classes

"""
There are 3 classes: Game, Player and Question.

game object
            --> player object
            --> game logic loop
                                --> question objects
"""

import random
import time


class Game:
    def __init__(self):
        self.player = Player()
        self.player.score = 0
        self.count = 0
        self.end = ""
        random.seed(time.time())  # to generate new sets of random numbers in each run
        self.game_logic()

    def game_logic(self):
        print("\n----------- ARITHMETIC GAME -----------\n")

        while self.end != "x":
            self.count += 1
            q = Question()
            self.player.score += q.check()
            self.end = input("\nx to exit, ENTER to continue\t")

        print("\n-----------------------------------------")
        print("\tYour score is {} out of {}".format(self.player.score, self.count))
        print("-----------------------------------------")


class Player:
    """
    Player object has a name and score
    """
    def __init__(self):
        self.name = input("Enter name: ")
        self.score = 0


class Question:
    """
    Question object has 2 random numbers a and b, an expression from the numbers [a + b =],
    a correct answer, an answer from the user/player, a function for getting user's answer
    input and a function for checking if the user's answer is correct.
    """
    def __init__(self):
        self.num_a = random.randint(0, 9)
        self.num_b = random.randint(0, 9)
        self.expression = "{} + {} =".format(self.num_a, self.num_b)
        self.ans = self.num_a + self.num_b
        self.player_ans = self.get_answer()

    def get_answer(self):
        return input("\n" + self.expression + " ")

    def check(self):
        if int(self.player_ans) == self.ans: return 1
        else: return 0


game = Game()
