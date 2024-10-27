# Задача "А как делить?"/true
from math import inf
def divide(first, second):
    if second == 0 and first > 0:
        division = inf
        print(f'{division} """БЕСКОНЕЧНОСТЬ - ЭТО НЕ ПРЕДЕЛ!"""')
    elif second == 0 and first < 0:
        division = -inf
        print(f'{division} """БЕСКОНЕЧНОСТЬ - ЭТО НЕ ЧЕРНАЯ ДЫРА!"""')
    else:
        division = first/second
        print(division)