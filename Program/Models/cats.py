from Program.Models.PetsABS import PetsABS


class Cats(PetsABS):
    '''Класс кошки'''

    def __init__(self, name, birthday, command):
        super().__init__(name, birthday, command)

    def eat(self):
        """Кошка умеет есть"""
        pass

    def speak(self):
        """Кошка умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'Кошка: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birthday()}, '
              f'команды - {self.get_command()}')
