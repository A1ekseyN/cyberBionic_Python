# Ready
iterable = range(1, 11)
iter_obj = iter(iterable)

while True:
    try:
        i = next(iter_obj)
        print(f"Число: {i}")
    except StopIteration:
        break
