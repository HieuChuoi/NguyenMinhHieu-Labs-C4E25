from random import *
import sys
sys.path.append('../')
from calc import eval

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 9)
    y = randint(0, 9)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    r = eval(x, y, op) + error
    return [x, y, op, r]

def check_answer(x, y, op, result, user_choice):
    correct_result = eval(x, y, op)
    if result == correct_result:
        if user_choice == True:
            return True
        elif user_choice == False:
            return False
    elif result != correct_result:
        if user_choice == True:
            return False
        elif user_choice == False:
            return True
