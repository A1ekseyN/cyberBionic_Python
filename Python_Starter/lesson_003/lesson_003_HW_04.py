# Ready
import math

print("Вы можете выбрать из нескольких операций:"
          "\n+, -, *, /, "
          "**(pow), √(квадратный корень), ∛(кубический корень), синус(sin), косинус(cos), тангенс(tan).")
result = input("\nВыберите операцию и перечисленных выше: ").lower()

if result == '+' or result == '-' or result == '*' or result == '/' or result == '**' or result == 'pow':
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
else:
    a = float(input("Введите число: "))

if result == '+':
    print(f"Результат: {a + b}")
elif result == '-':
    print(f"Результат: {a - b}")
elif result == '*':
    print(f"Результат: {a * b}")
elif result == '/':
    if b == 0:
        print("Деление на 0 не возможно.")
    else:
        print(f"Результат: {a / b}")
elif result == '**' or result == 'pow':
    print(f"Результат: {a ** b}")
elif result == '√' or result == 'квадратный корень':
    print(f"Результат. Квадратный корень из числа {a} = {math.sqrt(a)}")
elif result == 'кубический корень' or result == 'куб' or result == '∛':
    print(a ** (1./3.))
elif result == 'синус' or result == 'sin':
    print((a / 180) * math.pi)
elif result == 'косинус' or result == 'кос' or result == 'cos':
    print(math.cos(a))
elif result == 'тангенс' or result == 'tan':
    print(math.tan(a))
