# This is a simple Arithmetic quiz with score-keeping
# Python concepts: variables, data types, user input, if...else decision, loop, random

import random
import time

print("\n----------- ARITHMETIC GAME -----------\n")
name = input("Enter name: ")
score = 0
count = 0
end = ""

random.seed(time.time()) # to generate new sets of random numbers in each run

while end != "x":
    count += 1
    a = random.randint(0, 9)
    b = random.randint(0, 9)

    answer = input("\n" + str(a) + " + " + str(b) + " = ")
    print(a, "+", b, "=", a+b)
    if int(answer) == a+b: score += 1

    end = input("\nx to exit, ENTER to continue\t")

print("\n-----------------------------------------")
print("\tYour score is {} out of {}".format(score, count))
print("-----------------------------------------")
