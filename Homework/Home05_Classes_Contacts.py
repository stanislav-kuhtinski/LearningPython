__author__ = 'stanislav-kuhtinski'


class Person(object):

    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.contacts_list = []

    def add_contact(self, person):
        if not person in self.contacts_list:
            self.contacts_list.append(person)
            print('{} has been successfully added to the list!'.format(person.name))
        else:
            print('{} is already in your contact list!'.format(person.name))

    def find_contact(self, person):
        if person in self.contacts_list:
            print('Contact already in the list!')
        else:
            print('Contact not in the list')

    def display_contacts(self):
        for contacts_list in self.contacts_list:
            print(contacts_list)


new1 = Person('Peter', 30)
new2 = Person('Olga', 26)

new1.find_contact(new2)
new1.add_contact(new2)
new1.find_contact(new2)
new1.add_contact(new2)