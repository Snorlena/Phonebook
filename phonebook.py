#phonebooks are so 1990.. >_<

def print_phonebook():
    print('Name',':', 'Phone number')
    for x, y in phonebook.items():
        print(x,':', y, end='')

def add_contact():
    f = open ('phonebook.txt', 'w')
    name = input('Enter name: ')
    phone_number = input('Enter phone number: ')
    phonebook[name] = phone_number + '\n'
    for x, y in phonebook.items():
        f.write(x + ':' + y)

if __name__ == '__main__':
    phonebook = {}
    f = open ('phonebook.txt', 'r') 
    for line in f:
        split_line = line.split(':')
        phonebook[split_line[0]] = split_line[1]

    while True:
        print('What do you want to do?')
        print('Check phonebook(1)')
        print('Add contact(2)')
        do_what = input('> ')

        if do_what == '1':
            print_phonebook()
        elif do_what == '2':
            add_contact()
        else:
            print('Wrong input...')
            break