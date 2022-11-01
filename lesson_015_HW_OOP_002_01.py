# Ready
document_01 = ['Lorem Ipsum: Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci...']
serial_pro = 123
serial = 0

def menu():
    # Функция меню
    global menu
    menu = int(input("Выберите, что нужно сделать с документом:"
                     "\n1. Отобразить содержимое документа."
                     "\n2. Редактировать содержимое документа"
                     "\n3. Введите серийный номер для Pro версии"
                     "\n-- Выберете пункт меню: "))

menu()


class Editor():
    # Клаcс для отображения документа в бесплатной версии
    @staticmethod
    def view_document():
        return print(document_01)

    @staticmethod
    def edit_document():
        return print("\nРедактирование документа не возможно для бесплатной версии.")


class ProEditor():
    # Класс для платной версии
    @staticmethod
    def edit_document_pro():
        global document_01
        if serial == serial_pro:
            document_01 = input('Введите новое содержимое для документа: ')


if menu == 1:
    Editor.view_document()
elif menu == 2:
    Editor.edit_document()
elif menu == 3:
    menu = 0
    serial = int(input('\nВведите серийный номер для продукта (123): '))
    if serial == serial_pro:
        print('\nТеперь вы можете редактировать документ.')
        ProEditor.edit_document_pro()
        print('\nДокумент теперь содержит следующую информацию: ')
        print(document_01)
    elif serial != serial_pro:
        print(f'\nСерийный номер не верный. Попробуйте ввести серийный номер: {serial_pro}.')
        print('Тут можно обернуть в цикл while. Чтобы программа работала дальше.')
