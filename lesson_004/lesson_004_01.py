a = 0
b = 0
d = 1
count = 0
while True:
    a = int(input("Введите 10 цифр: "))
    b += a
    d *= a
    count += 1
    if count >= 10:
        break
print(f"Сумма {b} Добуток: {d}")