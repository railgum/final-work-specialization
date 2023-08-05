from abc import ABC, abstractmethod


class Animals(ABC):
    """Абстрактный класс Животные (Друзья человека)"""

    def __init__(self, name, birthday, command):
        self.__name = name
        self.__birthday = birthday
        self.__command = command

    def get_name(self) -> str:
        return self.__name

    def get_birthday(self) -> str:
        return self.__birthday

    def get_command(self) -> str:
        return self.__command

    @abstractmethod
    def print_animal(self):
        """Распечатать свойства животного"""
        pass
