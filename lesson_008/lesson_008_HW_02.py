# Ready
a = -5
status = True


def func_a():
    global a
    a += 0.5


def func_b():
    global status
    if a >= 5:
        status = False


while status:
    if a == -5:
        print(f"Число: {float(a)}")
    func_a()
    func_b()
    print(f"Число: {a}")
