a = int(input("Введите число: "))

if a % 10 == 0:
    print("Число делится на 10")
elif a % 5 == 0:
    print("Число делится на 5")
elif a % 3 == 0:
    print("Число делится на 3")
else:
    print(a)
