from my_package import display
from my_package import help
from my_package import select
from my_package import add


def getting_started():
    # Список людей
    people = []

    # zodiac_signs = {
    #             'name': "овен",
    #             'data_beg': datetime.datetime.strptime("11.11", "%d.%m"),
    #             'data_end': "birth"
    #         }
    # print(zodiac_signs.get("data_beg"))

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        # На Python с помощью ANSI-код можно делать цвет, фон и т.д.
        # \033[0m - сброс форматирования
        command = input("\033[0mEnter command: ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        # Добавить нового человека
        elif command == 'add':
            human = add.add_human()
            # Добавить словарь в список.
            people.append(human)

            # Отсортировать список в случае необходимости.
            # Сортировка по дате рождения (от старшего к младшим)
            if len(people) > 1:
                people.sort(key=lambda item: item.get('birth', ''))

        # Показать список людей
        elif command == 'show':
            display.display_people(people)

        # .startswith - Поиск строк с заданным началом строки
        elif command.startswith('select'):
            select.select_zz(command, people)

        # Список команд с описанием
        elif command == 'help':
            help.help_inf()

        # Неопознанная команда
        else:
            print("\033[31mUnknown command")
