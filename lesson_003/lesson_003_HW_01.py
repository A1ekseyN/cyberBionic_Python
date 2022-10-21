# Ready
my_name = 'Алексей'
user_name = input(f"Привет. \nМеня зовут {my_name}. А как зовут тебя? ")

if my_name == user_name.title():
    print(f"\nПриятно познакомится {user_name.title()}. У нас с тобой одинаковые имена. :)")
elif my_name != user_name.title():
    print(f"\nПриятно познакомится {user_name.title()}.")
