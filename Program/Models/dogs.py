from Program.Models.PetsABS import PetsABS


class Dogs(PetsABS):
    '''Класс собаки'''

    def __init__(self, name, birthday, command):
        super().__init__(name, birthday, command)

    def eat(self):
        """Собака умеет есть"""
        pass

    def speak(self):
        """Собака умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Собака: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birthday()}, '
              f'команды - {self.get_command()}')
