# This is a simple Arithmetic quiz with score-keeping
# Python concepts: variables, data types, user input, if...else decision

print("\n----------- ARITHMETIC GAME -----------\n")
name = input("Enter name: ")
score = 0
count = 0

# Question 1
a = 5
b = 7
answer = input("\n" + str(a) + " + " + str(b) + " = ")
print(a, "+", b, "=", a+b)
count += 1
if int(answer) == a+b:
    score += 1

# Question 2
a = 8
b = 3
answer = input("\n" + str(a) + " x " + str(b) + " = ")
print("{} x {} = {}".format(a, b, a*b))
count += 1
if int(answer) == a*b:
    score += 1

# Question 3
a = 54
b = 6
answer = input("\n" + str(a) + " - " + str(b) + " = ")
print("{} - {} = {}".format(a, b, a-b))
count += 1
if int(answer) == a-b:
    score += 1

print("\n-----------------------------------------")
print("\tYour score is {} out of {}".format(score, count))
print("-----------------------------------------")