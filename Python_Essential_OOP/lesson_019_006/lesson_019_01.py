a = range(0, 100)
b = []

def interator():
    cnt = 0
    for i in a:
        cnt += 1
        if cnt >= 5:
            b.append(i)
            cnt = 0

interator()
print(b)
