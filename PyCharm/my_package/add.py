import datetime


def add_human():
    # Кортеж ЗЗ
    zodiac_signs = (
        03.21,
        "овен",
        04.21,
        "телец",
        05.22,
        "близнецы",
        06.22,
        "рак",
        07.23,
        "лев",
        08.23,
        "дева",
        09.24,
        "весы",
        10.24,
        "скорпион",
        11.23,
        "стрелец",
        12.22,
        "козерог",
        01.21,
        "водолей",
        02.19,
        "рыбы",
        03.21
    )

    zs_ny = (
        12.22,
        "козерог",
        01.21,
        "водолей",
        02.19,
        "рыбы",
        03.21
    )

    # Запросить данные человека
    name = input("Enter name: ")
    # Проверка ЗЗ
    while True:
        zodiac_sign = input("\033[0mEnter zodiac sign: ").lower()
        if zodiac_sign not in zodiac_signs \
                and zodiac_sign not in zs_ny:
            print("\033[31mIncorrect zodiac sign")
        else:
            break

    # Проверка Даты Рождения
    while True:
        birth = input("\033[0mEnter date of birth (yyyy.mm.dd): ")
        # Обработка исключения (проверка правильности даты)
        try:
            birth_data = datetime.datetime.strptime(birth, '%Y.%m.%d')
        except Exception:
            print("\033[31mIncorrect data format")
        # Если ДР введен корректно относительно формата,
        # проверяем дату согласно ЗЗ
        else:
            # Получаем из кортежа начальную дату введенного ЗЗ
            # и преобразуем к нужному формату даты
            if zodiac_sign in zs_ny:
                beg_zs_data = datetime.datetime.strptime(
                    str(birth_data.year-1) + '.' +
                    str(zs_ny[zs_ny.index(zodiac_sign) - 1]),
                    '%Y.%m.%d'
                )
                # Получаем из кортежа конечную дату введенного ЗЗ
                # и преобразуем к нужному формату даты
                end_zs_data = datetime.datetime.strptime(
                    str(birth_data.year) + '.' +
                    str(zs_ny[zs_ny.index(zodiac_sign) + 1]),
                    '%Y.%m.%d'
                )
                # Сравнение введенной даты с промежутком дат ЗЗ
                if beg_zs_data <= birth_data < end_zs_data:
                    break
                else:
                    print("\033[31mEnter CORRECR date of birth "
                          "(yyyy.mm.dd): ")
            else:
                beg_zs_data = datetime.datetime.strptime(
                    str(birth_data.year) + '.' +
                    str(zodiac_signs[zodiac_signs.index(zodiac_sign) - 1]),
                    '%Y.%m.%d'
                )
                # Получаем из кортежа конечную дату введенного ЗЗ
                # и преобразуем к нужному формату даты
                end_zs_data = datetime.datetime.strptime(
                    str(birth_data.year) + '.' +
                    str(zodiac_signs[zodiac_signs.index(zodiac_sign) + 1]),
                    '%Y.%m.%d'
                )
                # Сравнение введенной даты с промежутком дат ЗЗ
                if beg_zs_data <= birth_data < end_zs_data:
                    break
                else:
                    print("\033[31mEnter CORRECR date of birth "
                          "(yyyy.mm.dd): ")
    # Вернуть словарь
    return {
        'name': name,
        'zodiac_sign': zodiac_sign,
        'birth': birth,
    }