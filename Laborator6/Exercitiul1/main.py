class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'Contact({self.name}, {self.email})'


class Agenda:
    all_contacts = ContactList()

    def add_contact(self, contact):
        self.all_contacts.append(contact)

    def print_agenda(self):
        for contact in self.all_contacts:
            print(contact)


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self):
        return f'Friend({self.name}, {self.email}, {self.phone})'


if __name__ == '__main__':
    agenda = Agenda()

    done = False

    while not done:
        print('=== Agenda v2.14 ===')
        print('1) Adauga contact')
        print('2) Adauga prieten')
        print('3) Afiseaza tote contactele (inclusiv prietenii)')
        print('4) Cauta un contact')
        print('5) Exit')

        choice = input('Choice: ')

        match int(choice):
            case 1:
                name = input('Name: ')
                email = input('Email: ')
                agenda.add_contact(Contact(name, email))
            case 2:
                name = input('Name: ')
                email = input('Email: ')
                phone = input('Phone number: ')
                agenda.add_contact(Friend(name, email, phone))
            case 3: agenda.print_agenda()
            case 4:
                name = input('Name: ')
                print(agenda.all_contacts.search(name))
            case 5: done = True
