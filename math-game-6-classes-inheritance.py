# This is a simple Arithmetic quiz
# Python concepts: variables, data types, user input, if...else decision,
# loop, random, functions, class inheritance

"""
There are 6 classes: Game, Player and Question parent class with 3 child classes for QAdd, QSubtract and QMultiply.

game object
            --> player object
            --> game logic loop
                                --> question base/parent class
                                    --> QAdd child class
                                    --> QSubtract child class
                                    --> QMultiply child class
"""

import random
import time


class Game:
    def __init__(self):
        self.player = Player()
        self.score = 0
        self.count = 0
        self.end = ""
        self.game_logic()

    def game_logic(self):
        print("\n----------- ARITHMETIC GAME -----------")

        while self.end != "x":
            self.ask(QAdd())
            if self.end != "x": self.ask(QSubtract())
            if self.end != "x": self.ask(QMultiply())

        print("\n-----------------------------------------")
        print("\tYour score is {} out of {}".format(self.score, self.count))
        print("-----------------------------------------")

    def ask(self, obj):
        # some question
        self.count += 1
        q = obj
        self.score += q.check()
        self.end = input("\nx to exit, ENTER to continue\t")


class Player:
    """
    Player object has a name and score
    """
    def __init__(self):
        self.name = input("Enter name: ")


class Question:
    """
    Base or parent class
    """
    def __init__(self):
        self.num_a = random.randint(0, 9)
        self.num_b = random.randint(0, 9)

    def get_answer(self):
        return input("\n" + self.expression + " ")

    def check(self):
        if int(self.player_ans) == self.answer: return 1
        else: return 0


class QAdd(Question):
    def __init__(self):
        super().__init__()
        self.answer = self.num_a + self.num_b
        self.expression = "{} + {} =".format(self.num_a, self.num_b)
        self.player_ans = self.get_answer()


class QSubtract(Question):
    def __init__(self):
        super().__init__()
        self.answer = self.num_a - self.num_b
        self.expression = "{} - {} =".format(self.num_a, self.num_b)
        self.player_ans = self.get_answer()


class QMultiply(Question):
    def __init__(self):
        super().__init__()
        self.answer = self.num_a * self.num_b
        self.expression = "{} x {} =".format(self.num_a, self.num_b)
        self.player_ans = self.get_answer()


random.seed(time.time())  # to generate new sets of random numbers in each run
game = Game()
