from mysql.connector import connect, Error


def select_table_dogs(config):
    """Распечатать пункт меню dogs"""
    try:
        with connect(
                host=config[0],
                user=config[1],
                password=config[2],
                database=config[3],
        ) as connection:
            select_dogs = "SELECT dogs_id, dog_name, dog_birthday, command_name FROM dogs LIMIT 5"
            with connection.cursor() as cursor:
                cursor.execute(select_dogs)
                result = cursor.fetchall()
                for row in result:
                    print(
                        f"Собака: id - {row[0]}, кличка - {row[1]}, родилась - {row[2]}, команды - {row[3]} ")
    except Error as e:
        print(e)


def select_table_cats(config):
    """Распечатать пункт меню cats"""
    try:
        with connect(
                host=config[0],
                user=config[1],
                password=config[2],
                database=config[3],
        ) as connection:
            select_cats = "SELECT cats_id, cat_name, cat_birthday, command_name FROM cats LIMIT 5"
            with connection.cursor() as cursor:
                cursor.execute(select_cats)
                result = cursor.fetchall()
                for row in result:
                    print(
                        f"Кошка: id - {row[0]}, кличка - {row[1]}, родилась - {row[2]}, команды - {row[3]} ")
    except Error as e:
        print(e)


def select_table_hamsters(config):
    """Распечатать пункт меню hamsters"""
    try:
        with connect(
                host=config[0],
                user=config[1],
                password=config[2],
                database=config[3],
        ) as connection:
            select_hamsters = "SELECT hamsters_id, hamster_name, hamster_birthday, command_name FROM hamsters LIMIT 5"
            with connection.cursor() as cursor:
                cursor.execute(select_hamsters)
                result = cursor.fetchall()
                for row in result:
                    print(
                        f"Хомяк: id - {row[0]}, кличка - {row[1]}, родилась - {row[2]}, команды - {row[3]} ")
    except Error as e:
        print(e)


def select_table_horses(config):
    """Распечатать пункт меню horses"""
    try:
        with connect(
                host=config[0],
                user=config[1],
                password=config[2],
                database=config[3],
        ) as connection:
            select_horses = "SELECT horses_id, horse_name, horse_birthday, command_name FROM horses LIMIT 5"
            with connection.cursor() as cursor:
                cursor.execute(select_horses)
                result = cursor.fetchall()
                for row in result:
                    print(
                        f"Лошадь: id - {row[0]}, кличка - {row[1]}, родилась - {row[2]}, команды - {row[3]} ")
    except Error as e:
        print(e)


def select_table_camels(config):
    """Распечатать пункт меню camels"""
    try:
        with connect(
                host=config[0],
                user=config[1],
                password=config[2],
                database=config[3],
        ) as connection:
            select_camels = "SELECT camels_id, camel_name, camel_birthday, command_name FROM camels LIMIT 5"
            with connection.cursor() as cursor:
                cursor.execute(select_camels)
                result = cursor.fetchall()
                for row in result:
                    print(
                        f"Верблюд: id - {row[0]}, кличка - {row[1]}, родилась - {row[2]}, команды - {row[3]} ")
    except Error as e:
        print(e)


def select_table_donkeys(config):
    """Распечатать пункт меню donkeys"""
    try:
        with connect(
                host=config[0],
                user=config[1],
                password=config[2],
                database=config[3],
        ) as connection:
            select_donkeys = "SELECT donkeys_id, donkey_name, donkey_birthday, command_name FROM donkeys LIMIT 5"
            with connection.cursor() as cursor:
                cursor.execute(select_donkeys)
                result = cursor.fetchall()
                for row in result:
                    print(
                        f"Осел: id - {row[0]}, кличка - {row[1]}, родилась - {row[2]}, команды - {row[3]} ")
    except Error as e:
        print(e)


def print_animal(config):
    """Выбрать и распечатать таблицу со списком животных"""
    flag = -1
    while flag == -1:
        print('\nSelect the menu item by entering the appropriate number:\n'
              '1. Pets\n'
              '2. Pack animals\n'
              '3. Go back\n')

        user_input = input('Enter: ')
        if user_input.isdigit():
            match int(user_input):
                case 1:
                    while flag:
                        print('\nSelect the menu item by entering the appropriate number:\n'
                              '1. Dogs\n'
                              '2. Cats\n'
                              '3. Hamsters\n'
                              '4. Go back\n')

                        user_input = input('Enter: ')
                        if user_input.isdigit():
                            match int(user_input):
                                case 1:
                                    select_table_dogs(config)
                                    flag = [1, 1]
                                    return flag
                                case 2:
                                    select_table_cats(config)
                                    flag = [2, 1]
                                    return flag
                                case 3:
                                    select_table_hamsters(config)
                                    flag = [3, 1]
                                    return flag
                                case 4:
                                    break
                        else:
                            print('\nYou entered the wrong number. Try again.')
                case 2:
                    while flag:
                        print('\nSelect the menu item by entering the appropriate number:\n'
                              '1. Horses\n'
                              '2. Camels\n'
                              '3. Donkeys\n'
                              '4. Go back\n')

                        user_input = input('Enter: ')
                        if user_input.isdigit():
                            match int(user_input):
                                case 1:
                                    select_table_horses(config)
                                    flag = [1, 2]
                                    return flag
                                case 2:
                                    select_table_camels(config)
                                    flag = [2, 2]
                                    return flag
                                case 3:
                                    select_table_donkeys(config)
                                    flag = [3, 2]
                                    return flag
                                case 4:
                                    break
                        else:
                            print('\nYou entered the wrong number. Try again.')
                case 3:
                    break
        else:
            print('\nYou entered the wrong number. Try again.')
