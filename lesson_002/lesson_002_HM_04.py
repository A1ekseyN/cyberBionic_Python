# Ready
a = input("Введите 10 символов: ")
ascii_sum = 0

for i in a:
    ascii_sum += ord(i)

print(f"ASCII сумма 10-ти символов: {ascii_sum}.")
