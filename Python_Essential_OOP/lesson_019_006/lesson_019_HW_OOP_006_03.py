# Ready
iterable = range(1, 11)
iter_obj = iter(iterable)
list = []

for i in iter_obj:
    list.append(i)
list = reversed(list)

while True:
    try:
        i = next(list)
        print(f"Число: {i}")
    except StopIteration:
        break
