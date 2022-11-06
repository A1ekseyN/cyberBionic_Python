class MyList(object):

    class _ListNode(object):
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return f"MyList._ListNode_New {self.value}, {self.prev}, {self.next}"

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def get_by_index(self, ind):
        index = self._head
        index_counter = 0
        try:
            while index_counter <= ind:
                if index_counter == ind:
                    return index.value
                index_counter += 1
                index = index.next
        except:
            print('Нет значения за этим индексом.')

    # Метод очистки списка
    def clear(self):
        self._head = None
        self._tail = None
        self._length = 0

    def insert_index(self, ind, data):
        if self._head is None:
            print('Список пустой')
            return
        else:
            index = self._head
            index_counter = 0
            try:
                while index_counter <= ind:
                    if index_counter == ind:
                        index.value = data
                    index_counter += 1
                    index = index.next
            except:
                print('Индекса нет в списке.')

    # Вставить значение после определенного индекса
    def insert_after_item(self, x, data):
        if self._head is None:
            print('Список пуст.')
            return
        else:
            n = self._head
            while n is not None:
                if n.value == x:
                    break
                n = n.next
            if n is None:
                print('Данного значения нет в списке.')
            else:
                new_node = MyList._ListNode(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    # Метод удаления последнего элемента списка
    def del_end(self):
        if self._head is None:
            print('Список пустой.')
            return
        if self._head.next is None:
            self._head = None
            return
        n = self._head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    # Метод удаления значения по индексу
    def del_index(self, ind):
        index = self._head
        index_counter = 0
        while index_counter <= ind:
            if index_counter == ind:
                if ind == 0:
                    self._head = index.next
                else:
                    index.prev.next = index.next
            index_counter += 1
            index = index.next

    def append(self, element):
        """Добавление элемента в конец списка"""
        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    my_list = MyList([1, 2, 5, 8, 10])
    print(f'Длина списка: {len(my_list)}')
    print(f'Список: {my_list}\n')

    for i in my_list:
        print(f'{i}', end=', ')
    print()

    my_list.insert_index(1, 4)
    print(f'Добавили в список 1, 4: {my_list}')
    print(f'Поиск по значению: {my_list.get_by_index(2)}')

    my_list.del_index(0)
    print(f"{my_list}")

    my_list.insert_after_item(4, 1)
    print(f"Вставляем значение после 4: {my_list}")

    my_list.del_end()
    print(f"После удаления последнего элемента: {my_list}")

    my_list.clear()
    print(f'Список после очистки: {my_list}')

if __name__ == '__main__':
    main()
