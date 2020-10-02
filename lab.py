from collections import namedtuple

book = namedtuple('book', 'name, author, year, length')
note = []

def get_index(name):
    try:
        index = [True if x.name==name else False for x in note ].index(True)
    except ValueError as e:
        print(f'{name} was not found')
        return None
    return index

def add(name, author, year, length):
    note.append(book(name, author, year, length))

def delete(name):
    index = get_index(name)
    try:
        note.pop(index)
    except TypeError as e:
        print('Nothing to delete')

def edit(name, feature, value):
    index = get_index(name)
    try:
        if feature == 'name':
            note[index] = note[index]._replace(name=value)
        elif feature == 'author':
            note[index] = note[index]._replace(author=value)
        elif feature == 'year':
            note[index] = note[index]._replace(year=value)
        elif feature == 'length':
            note[index] = note[index]._replace(length=value)
        else:
            print(f'No feature called {feature}')
    except TypeError as e:
        print('Nothing to edit')


def loop():
    print('Type in a command or "COMMAND LIST"')
    while True:
        command = input('-->')
        if command == 'COMMAND LIST':
            print('ADD book_name, author, year, length: add book to database\
                   \nDELETE book_name: delete book from database\
                   \nEDIT book_name, book_feature, value: edit book feature\
                   \nSHOW: show all books')
        elif command.startswith('ADD') == True:
            try:
                name, author, year, length = tuple(command[len('ADD')+1:].split(', '))
            except ValueError as e:
                print('Wrong syntax')
                continue
            add(name, author, year, length)
        elif command.startswith('DELETE') == True:
            try:
                name, = tuple(command[len('DELETE')+1:].split(', '))
            except ValueError as e:
                print('Wrong syntax')
                continue
            delete(name)
        elif command.startswith('EDIT') == True:
            try:
                name, feature, value = tuple(command[len('EDIT')+1:].split(', '))
            except ValueError as e:
                print('Wrong syntax')
                continue
            edit(name, feature, value)
        elif command == 'SHOW':
            print('#')
            for book_ in note:
                print(book_)
            print('#')

if __name__ == '__main__':
    loop()
