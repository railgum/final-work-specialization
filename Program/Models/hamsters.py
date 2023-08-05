from Program.Models.PetsABS import PetsABS


class Hamsters(PetsABS):
    '''Класс хомяки'''

    def __init__(self, name, birthday, command):
        super().__init__(name, birthday, command)

    def eat(self):
        """Хомяк умеет есть"""
        pass

    def speak(self):
        """Хомяк умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Хомяк: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birthday()}, '
              f'команды - {self.get_command()}')