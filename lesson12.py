import argparse

book = {"Nastya": 89993457645, "Andrey": 8945614645, "Sasha": 89126581435}

parser = argparse.ArgumentParser(description="Telephone book")
parser.add_argument('-a', '--add', dest="param1")
parser.add_argument('-d', '--delete', dest="param2")
parser.add_argument('-s', '--show', dest="param3", default='all')
 
args = parser.parse_args()

if args.param1:
    name, t_number = args.param1.split(":")
    if name in book:
        book[name] [book.get(name), int(t_number)] 
        print("Контанкт с именем ", name, " обновлён")
        print(name, ":", book[name])
    else:
        book[name] = int(t_number)
        print("Контанкт с именем ", name, " добавлен")
        print(name, ":", book[name])

if args.param2:
    if args.param2 in book:    
         book.pop(args.param2)
         print("Контанкт с именем ", name, " удалён")
         print(book)
    else:
        print('Контакта с таким именем не существует')

if args.param3:
    if args.param3 == 'all':
        print(book)
    elif args.param3 in book:
        print(args.param3, ":", book.get(args.param3))
    else:
        print('Контакта с таким именем не существует')


