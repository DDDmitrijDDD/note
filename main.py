from db import db_map as db
print("*" * 10, "Заметки", "*" * 10)
print("Команды:", "Список заметок", "Добавить заметку", "Найти заметку", "Удалить заметку", "Для выхода напишите 'q'",
      "Введите команду ", sep='\n')
while True:
    global command
    command = input("")
    if command == "q":
        break

    all_name = []
    for i in db.all_notes():
        for j in i:
            all_name.append(j)

    def list_notes():
        # проверяем есть ли заметки или нет
        if not db.all_notes():
            print("Нету ни одной заметки, создайте первую!")
        else:
            # если есть, то выводим название всех заметок
            for i in db.all_notes():
                for j in i:
                    print(j)
            name = input("Напишите название заметки, которую хотите открыть или же напишите q ")
            if name == "q":
                print("Команды:", "Список заметок", "Добавить заметку", "Найти заметку", "Удалить заметку",
                      "Для выхода напишите 'q'",
                      "Введите команду ", sep='\n')
                # проверяем есть ли такая заметка какую ввел пользователь и выводим ее содержимое если есть
            else:
                if name in all_name:
                    for i in db.note(name):
                        print(i)
                else:
                    print("Такой заметки не существует")


    def add_note():
        # просим ввести название, если такой заметки нету, просим ввести содержимое заметки и заносим информацию в бд
        name = input("Введите название заметки ")
        if name in all_name:
            print("Заметка с таким названием уже существует")
        else:
            text = input("Введите содержимое заметки")
            db.add_note(name, text)
            print("заметка успешно добавлена!")


    def search_note():
        # проверяем есть ли введенный текст в заметках и выводим название заметок в которых данный текст присутствует
        note = []
        text = input("Введите слово или фразу, чтобы найти заметку ")
        for i in db.search_note():
            if text in i[2]:
                note.append(i[1])
        if not note:
            print("Заметки в которой втречается это слово или фраза не нашлось")
        else:
            print("Это слово или фраза встречается в этих заметках:")
            for i in note:
                print(i)

    def delete_note():
        for i in db.all_notes():
            for j in i:
                print(j)
        name = input("Введите название заметки которую хотите удалить ")
        # проверяем существует ли введенная заметка и если да, то удаляем ее и ее содержание
        if name in all_name:
            db.delete_note(name)
            print(f"Заметка '{name}' удалена")
        else:
            print("Такой заметки не существует!")

    if command == "Список заметок":
        list_notes()

    if command == "Добавить заметку":
        add_note()

    if command == "Найти заметку":
        search_note()

    if command == "Удалить заметку":
        delete_note()


