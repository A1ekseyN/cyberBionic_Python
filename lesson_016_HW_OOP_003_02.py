# Ready
class English_greeting():
    @staticmethod
    def greeting():
        return print("Hello World from England.")


class Spanish_greeting():
    @staticmethod
    def greeting():
        return print("Hola Mundo desde Inglaterra.")


def hello_friend():
    English_greeting.greeting()
    Spanish_greeting.greeting()


hello_friend()
