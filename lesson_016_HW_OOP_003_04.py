# Ready
class Base:
    @classmethod
    def hello(cls):
        return print('Hello from Base.')


class Child(Base):
    @classmethod
    def hello(cls):
        return print('Hello from Child.')


Base.hello()
Child.hello()
