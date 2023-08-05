from Program.Models.PackAnimalsABS import PackAnimalsABS


class Horses(PackAnimalsABS):
    '''Класс лошади'''

    def __init__(self, name, birthday, command):
        super().__init__(name, birthday, command)

    def eat(self):
        """лошадь умеет есть"""
        pass

    def speak(self):
        """лошадь умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'лошадь: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birthday()}, '
              f'команды - {self.get_command()}')