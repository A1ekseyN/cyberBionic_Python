# Ready
from math import pi
from math import e


number = 5
count = int(input('Введите количество повторов: '))

print(number * count)
print(pi * number * count)
print(e * 2)

while number >= 0:
    number -= 1

string = 'my string'
sum_ = 0

for i in string:
    sum_ += pow(string.find(i), 2)
    print("sum =", sum_)


def my_function(atr=1):
    print('atr', atr)


print(my_function(atr=5))
