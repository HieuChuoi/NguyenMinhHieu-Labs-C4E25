from random import *
# import calc
from calc import eval

# Sinh bieu thuc
x = randint(0, 9)
y = randint(0, 9)
op = choice(["+", "-", "*", "/"])
error = randint(-1, 1)
# r = calc.eval(x, y, op) + error
r = eval(x, y, op) + error

print(x, op, y, "=", r)

user_input = input("Your answer (Y/N)").upper()

result = ""
if error == 0:
    if user_input == "Y":
        result = "Yay"
    else:
        result = "Nay"
else:
    if user_input == "Y":
        result = "Nay"
    else:
        result = "Yay"

print(result)