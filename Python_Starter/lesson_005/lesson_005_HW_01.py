# Ready
first_name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')

if first_name.isalpha() and last_name.isalpha():
    if first_name[0].isupper() and last_name[0].isupper():
        print(f'\nВсе правильно.\nВы ввели имя и фамилию: {first_name} {last_name}.')
    elif first_name[0].isupper() and not last_name[0].isupper():
        print('\nВаше имя написано верно, а фамилия не верно.\nПроверьте написание фамилии.')
    elif last_name[0].isupper() and not first_name[0].isupper():
        print('\nВаша фамилия написана верно, а имя не верно.\nПроверьте написание имени.')
    else:
        print('\nВаше имя и фамилия написаны не верно.\nНапишите имя и фамилию с больших букв.')
else:
    print('\nВы используете цифры в имени и фамилии.')
