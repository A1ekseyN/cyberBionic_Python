# Ready
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
result = float(input("Введите значение c: "))

discriminant = (b ** 2) - (4 * a * result)

print(f"Дискриминант = {discriminant}.")

if discriminant < 0:
    print("Нет корней.")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"x = {x}.")
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f"x1 = {x1}.")
    print(f"x2 = {x2}.")
