# Ready
login = 'login'
password = 'password'
attempt_count = 3

for i in range(attempt_count):
    login_try = input('Введите логин: ')
    password_try = input('Введите пароль: ')
    print()
    if login == login_try and password == password_try:
        print(f'Авторизация успешна за {i + 1} попыток.')
        break
    elif i + 1 == attempt_count:
        print('Вы исчерпали количество попыток. Попробуйте позже.')
