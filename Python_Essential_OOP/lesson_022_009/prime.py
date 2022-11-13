from ask_number import *


n = ask_number()


def prime():
    list = []

    for i in range(2, n + 1):
        for j in list:
            if i % j == 0:
                break
        else:
            list.append(i)
    return list
