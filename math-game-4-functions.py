# This is a simple Arithmetic quiz
# Python concepts: variables, data types, user input, if...else decision, loop, random, functions

import random
import time


def get_numbers():
    return random.randint(0, 9), random.randint(0, 9)


def question_addition(a, b, cnt, scr):
    expr = "{} + {} =".format(a, b)
    ans = a + b
    player_ans = input("\n" + expr + " ")
    if int(player_ans) == ans: scr += 1
    else: print(expr, ans)
    return cnt + 1, scr


def question_subtraction(a, b, cnt, scr):
    expr = "{} - {} =".format(a, b)
    ans = a - b
    player_ans = input("\n" + expr + " ")
    if int(player_ans) == ans: scr += 1
    else: print(expr, ans)
    return cnt + 1, scr


def question_multiplication(a, b, cnt, scr):
    expr = "{} x {} =".format(a, b)
    ans = a * b
    player_ans = input("\n" + expr + " ")
    if int(player_ans) == ans: scr += 1
    else: print(expr, ans)
    return cnt + 1, scr


def game_logic():
    print("\n----------- ARITHMETIC GAME -----------\n")
    name = input("Enter name: ")
    score = 0
    count = 0
    end = ""
    random.seed(time.time())  # to generate new sets of random numbers in each run

    while end != "x":
        a, b = get_numbers()
        count, score = question_addition(a, b, count, score)
        count, score = question_subtraction(a, b, count, score)
        count, score = question_multiplication(a, b, count, score)
        end = input("\nx to exit, ENTER to continue\t")

    print("\n-----------------------------------------")
    print("\tYour score is {} out of {}".format(score, count))
    print("-----------------------------------------")


game_logic()