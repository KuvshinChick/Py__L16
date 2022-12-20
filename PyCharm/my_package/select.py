def select_zz(com, people_list):
    # Разбить команду на части для выделения номера года.
    # Параметр maxsplit - int, сколько раз делить строку.
    while True:
        parts = com.split(' ', maxsplit=1)
        if len(parts) == 1:
            com = input("\033[31mEnter command "
                        "select and Zodiac_sign: ").lower()
            # Получить требуемый ЗЗ.
        else:
            break

    # Инициализировать счетчик.
    count = 0
    zz = parts[1]
    # Заголовок таблицы.
    line = (f'\033[0m{"+" + "-" * 12 + "+" + "-" * 12 + "+"}'
            f'{"-" * 15 + "+"}')
    print(line)
    print(
        f"|{'Name' :^12}|{'Birth ' :^12}"
        f"|{'Zodiac_sign ' :^15}|"
    )
    print(line)
    # Таблица с людьми
    for p in people_list:
        if zz == p.get('zodiac_sign'):
            count += 1
            print(
                f'|{p.get("name", "") :^12}|'
                f'{p.get("birth", "") :^12}|'
                f'{p.get("zodiac_sign", "") :^15}|'
            )
            print(line)

    # Если счетчик равен 0, то люди не найдены.
    if count == 0:
        print("Люди с заданным ЗЗ не найдены")
