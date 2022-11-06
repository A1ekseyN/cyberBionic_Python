# Ready
class Contact:
    # Класс контакта
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def __str__(self):
        return f'Full name: {self.name} {self.surname}\nAge: {self.age}\nMobile phone: {self.mob_phone}' \
               f'\nEmail: {self.email}\n'

    def get_contact(self):
        return f'Test message for get_contact'

    def send_message(self):
        return f'Send message to contact.'


class Update_Contact(Contact):
    def get_message(self):
        pass


contact_01 = Contact('Zemeckis', 'Robert', '70', '+380971277367', 'robby_1952@gmail.com')
contact_02 = Contact('Ritchie', 'Guy', '54', '+380973477467', 'ritchie_007@i.ua')

print(contact_01)
print(contact_02)

print(f'Test __dict__:\n{Contact.__dict__}\n')
print(f'Test __base__:\n{Contact.__base__}\n')
print(f'Test __bases__:\n{Update_Contact.__bases__}\n')

print(dir(Contact))

print(f"\nАтрибут класса - имя: {contact_01.surname} {contact_01.name}.")

job = "It's first job"
first_job = 'Python Developer'

setattr(Contact, job, first_job)
print(dir(Contact), '\n')
delattr(Contact, job)
print(dir(Contact))
print(dir(Update_Contact))
