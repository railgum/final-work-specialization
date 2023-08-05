from mysql.connector import *


class TeachNewCommands:
    """Класс обучить животное новым командам"""

    def __init__(self, new_command):
        self.__new_command = new_command

    def get_new_command(self) -> str:
        return self.__new_command

    def select_animal_command(self, config, type_a, a_id):
        """Получить запись поля command_name"""
        result = None
        try:
            with connect(
                    host=config[0],
                    user=config[1],
                    password=config[2],
                    database=config[3],
            ) as connection:
                select_dogs = f"SELECT command_name FROM {type_a}s WHERE {type_a}s_id = {a_id};"
                with connection.cursor() as cursor:
                    cursor.execute(select_dogs)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(e)

    def update_animal_command(self, config, type_a, a_id, old_comm):
        """Обновить запись поля comman_name"""
        try:
            with connect(
                    host=config[0],
                    user=config[1],
                    password=config[2],
                    database=config[3],
            ) as connection:
                update_command_name = f"""
                UPDATE {type_a}s SET command_name = "{old_comm[0][0]}, {self.__new_command}"  
                WHERE {type_a}s_id = {a_id};
                """
                with connection.cursor() as cursor:
                    cursor.execute(update_command_name)
                    connection.commit()
                    print(f'New command added!')
        except Error as e:
            print(e)

    def teach_new_command(self, config, animal_id, selected_animal):
        """Обучить новой команде"""
        if selected_animal[1] == 1:
            if selected_animal[0] == 1:  # dog
                type_a = 'dog'
                com = self.select_animal_command(config, type_a, animal_id)
                self.update_animal_command(config, type_a, animal_id, com)
            elif selected_animal[0] == 2:  # cat
                type_a = 'cat'
                com = self.select_animal_command(config, type_a, animal_id)
                self.update_animal_command(config, type_a, animal_id, com)
            else:  # hamster
                type_a = 'hamster'
                com = self.select_animal_command(config, type_a, animal_id)
                self.update_animal_command(config, type_a, animal_id, com)
        else:
            if selected_animal[0] == 1:  # horse
                type_a = 'horse'
                com = self.select_animal_command(config, type_a, animal_id)
                self.update_animal_command(config, type_a, animal_id, com)
            elif selected_animal[0] == 2:  # camel
                type_a = 'camel'
                com = self.select_animal_command(config, type_a, animal_id)
                self.update_animal_command(config, type_a, animal_id, com)
            else:  # donkey
                type_a = 'donkey'
                com = self.select_animal_command(config, type_a, animal_id)
                self.update_animal_command(config, type_a, animal_id, com)
