from Program.Models.PackAnimalsABS import PackAnimalsABS


class Camels(PackAnimalsABS):
    '''Класс верблюды'''

    def __init__(self, name, birthday, command):
        super().__init__(name, birthday, command)

    def eat(self):
        """Верблюд умеет есть"""
        pass

    def speak(self):
        """Верблюд умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Верблюд: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birthday()}, '
              f'команды - {self.get_command()}')
