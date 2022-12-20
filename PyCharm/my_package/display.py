def display_people(people_list):
    # Заголовок таблицы.
    line = (f'{"+" + "-" * 15 + "+" + "-" * 12 + "+"}'
            f'{"-" * 15 + "+"}')
    print(line)
    print(f"|{'Name' :^15}|{'Birth ' :^12}|{'Zodiac_sign ' :^15}|")
    print(line)

    # Вывести данные о всех людях.
    for idx, man in enumerate(people_list):
        print(
            f'|{man.get("name", "") :^15}'
            f'|{man.get("birth", "") :^12}'
            f'|{man.get("zodiac_sign", "") :^15}|'
        )
        print(line)