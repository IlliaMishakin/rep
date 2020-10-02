from collections import namedtuple

book = namedtuple('book', 'name, author, year, length')
note = []

def add(name, author, year, length):
    note.append(book(name, author, year, length))

def delete(name):
    try:
        index = [True for x in note if x.name==name].index(True)
    except ValueError as e:
        print('Book was not found')
        return None
    note.pop(index)

def edit(name, feature, value):
    try:
        index = [True for x in note if x.name==name].index(True)
    except ValueError as e:
        print('Book was not found')
        return None
    if feature == 'name':
        note[index] = note[index]._replace(name=value)
    elif feature == 'author':
        note[index] = note[index]._replace(author=value)
    elif feature == 'year':
        note[index] = note[index]._replace(year=value)
    elif feature == 'length':
        note[index] = note[index]._replace(length=value)


def loop():
    while True:
        command = input('Type in a command or "COMMAND LIST"\n-->')
        if command == 'COMMAND LIST':
            print('ADD book_name, author, year, length: add book to database\
                   \nDELETE book_name: delete book from database\
                   \nEDIT book_name, book_feature, value: edit book feature\
                   \nSHOW DB: show all books')
        elif command.startswith('ADD') == True:
            try:
                name, author, year, length = command[len('ADD'):].split(', ')
            except ValueError as e:
                print('Wrong syntax')
                continue
            add(name, author, year, length)
        elif command.startswith('DELETE') == True:
            try:
                name = command[len('DELETE'):].split(', ')
            except ValueError as e:
                print('Wrong syntax')
                continue
            delete(name)
        elif command.startswith('EDIT') == True:
            try:
                name, feature, value = command[len('EDIT'):].split(', ')
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
