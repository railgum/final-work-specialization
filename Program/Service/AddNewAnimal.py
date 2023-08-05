from mysql.connector import *

from Program.Models.AnimalsABS import Animals


class AddNewAnimal(Animals):
    """Класс новое животное"""

    def __init__(self, type_animal, name, birthday, command):
        self.__type_animal = type_animal
        super().__init__(name, birthday, command)

    def get_type_animal(self) -> str:
        return self.__type_animal

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birthday()}, '
              f'команды: {self.get_command()}')

    def new_pet(self, config, count):
        """Завести новое домашнее животное"""

        try:
            with connect(
                    host=config[0],
                    user=config[1],
                    password=config[2],
                    database=config[3],
            ) as connection:
                if self.__type_animal == 1:
                    table_name = 'dog'
                elif self.__type_animal == 2:
                    table_name = 'cat'
                else:
                    table_name = 'hamster'
                insert_type_animal_query = f"""
                INSERT INTO {table_name}s
                (domestic_animalsId, animalsId, {table_name}_name, {table_name}_birthday, command_name) 
                VALUES 
                ({self.get_type_animal()}, 1, "{self.get_name()}", "{self.get_birthday()}", "{self.get_command()}");
                """
                with connection.cursor() as cursor:
                    cursor.execute(insert_type_animal_query)
                    connection.commit()
                    count.add()
                    print(f'\nNew animal added!')
        except Error as e:
            print(e)

    def new_pack_animal(self, config, count):
        """Завести новое вьючное животное"""

        try:
            with connect(
                    host=config[0],
                    user=config[1],
                    password=config[2],
                    database=config[3],
            ) as connection:
                if self.__type_animal == 1:
                    table_name = 'horse'
                elif self.__type_animal == 2:
                    table_name = 'camel'
                else:
                    table_name = 'donkey'
                insert_type_animal_query = f"""
                INSERT INTO {table_name}s
                (pack_animalsId, animalsId, {table_name}_name, {table_name}_birthday, command_name) 
                VALUES 
                ({self.get_type_animal()}, 2, "{self.get_name()}", "{self.get_birthday()}", "{self.get_command()}");
                """
                with connection.cursor() as cursor:
                    cursor.execute(insert_type_animal_query)
                    connection.commit()
                    count.add()
                    print(f'\nNew animal added!')
        except Error as e:
            print(e)
