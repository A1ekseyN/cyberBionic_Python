# Ready
class Book():

    def __init__(self, author, title, year, genre):
        # Инициализируем атрибуты автора, названия, год, жарн
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"{self.author} {self.title} {self.year} {self.genre}"

    def __str__(self):
        return f"- {self.title}, автор - {self.author}, вышла в {self.year} году, в жарне - {self.genre}."


book_01 = Book('Джордж Оруэлл', '1984', '1949', 'Роман-антиутопия')
book_02 = Book('Мэттью Макконахи', 'Зеленый свет', '2020', 'Биография')
book_03 = Book('Эрих Берн', 'Игры в которые играют люди', '1964', 'Эссе')

print("В этом году я прочитал несколько книг. Вот несколько из них: ")
print(book_01)
print(book_02)
print(book_03)
