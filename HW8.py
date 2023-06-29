# Задача 38:
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


path: str = "phones"
phone_book = {}

def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name':nc[1], 'phone':nc[2], 'comment':nc[3]}
    print('\n Телефонная книга успешно загружена\n')

def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get("name"), contact.get("phone"), contact.get("comment")])
        data.append(new)
    data = "\n".join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print('\n Телефонная книга успешно сохранениа \n')

def search():
    result = {}
    word = input("Введите слово, по которому будет осуществляться поиск: ")
    for i, contact in phone_book.items():
        if word.lower() in " ".join(list(contact.values())).lower():
            result[i] = contact;
    return result

def remove():
    result = search()
    show_contact(result)
    if len(result) == 0:
        return
    index = int(input("Введите индекс контакта, который надо удалить: "))
    del_cnt = phone_book.pop(index)
    print(f'\nКонтакт {del_cnt.get("name")} удален.')
    print("\n" + "=" * 20)

def replasement():
    result = search()
    show_contact(result)
    if len(result) == 0:
        return
    index = int(input("Введите индекс контакта, который надо изменить: "))
    name = input("Введите новое имя контакта (пустое значение = не менять): ")
    phone = input("Введите новый номер телефона контакта: ")
    comment = input("Введите новый комментарий контакта : ")
    if len(name) == 0:
        name = phone_book[index].get('name')
    if len(phone) == 0:
        phone = phone_book[index].get('phone')
    if len(comment) == 0:
        comment = phone_book[index].get('comment')
    phone_book[index] = {'name': name, 'phone': phone, 'comment': comment}
    print(f'\nКонтакт {name} изменен.')
    print("\n" + "=" * 20)


def show_contact(book: dict[int, dict]):
    if len(book) == 0:
        print("\nКонтакты не найдены\n")
        return
    print("\n" + "=" * 20)
    for i, cnt in book.items():
        print(f'{i:>5}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print("=" * 20 + "\n")

def add_contact():
    cur_id = max(list(phone_book.keys())) + 1
    name = input("Введите имя контакта: ")
    phone = input("Введите телефон: ")
    comm = input("Введите комментарий: ")
    phone_book[cur_id] = {'name':name, 'phone':phone, 'comment':comm}
    print(f'\nКонтакт {name} успешно добавлен в книгу')
    print("\n" + "=" * 20)

def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контект
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input("Выберите пункт меню: ")
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print("Ошибка ввода, введите ЧИСЛО от 1 до 8: ")

open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contact(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contact(result)
        case 6:
            replasement()
        case 7:
            remove()
        case 8:
            print("До свидания!")
            break