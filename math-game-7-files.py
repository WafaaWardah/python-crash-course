# This is a simple Arithmetic quiz - highest score gets recorded in a txt file
# Python concepts: variables, data types, user input, if...else decision,
# loop, random, functions, class inheritance, datetime, file handling

import random
import time
import datetime
import os


class Game:
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.duration = None
        self.highest_score = 0
        self.top_player = ""
        self.player = Player()
        self.count = 0
        self.end = ""
        self.game_logic()

    def load_logs(self):
        if os.path.exists('log.txt') and os.stat('log.txt').st_size != 0:
            with open('log.txt', 'r') as log:
                buffer = log.read()
                self.top_player = buffer.split(sep=',')[0]
                self.highest_score = buffer.split(sep=',')[1]

    def save_logs(self):
        if self.player.score > int(self.highest_score):
            print("\tBravo! Highest score!!")
            with open('log.txt', 'w') as log:
                log.write(self.player.name + ',' + str(self.player.score))

    def game_logic(self):
        print("\n----------- ARITHMETIC GAME -----------")
        print("\tGood luck {}!".format(self.player.name))

        self.load_logs()

        while self.end != "x":
            self.ask(QAdd())
            if self.end != "x": self.ask(QSubtract())
            if self.end != "x": self.ask(QMultiply())

        self.duration = datetime.datetime.now() - self.start_time
        mins = self.duration.total_seconds() / 60
        secs = self.duration.total_seconds() % 60

        print("\n-----------------------------------------")
        self.save_logs()
        print("\tYour score is {} out of {}".format(self.player.score, self.count))
        print("\tTime taken: {} mins {} secs".format(round(mins), round(secs)))
        print("\tSee you again, {}!".format(self.player.name))
        print("-----------------------------------------")

    def ask(self, obj):
        # some question
        self.count += 1
        q = obj
        self.player.score += q.check()
        self.end = input("\nx to exit, ENTER to continue\t")


class Player:
    """
    Player object has a name and score
    """
    def __init__(self):
        self.name = input("\nEnter name: ")
        self.score = 0


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
