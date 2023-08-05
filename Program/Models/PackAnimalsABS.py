from abc import abstractmethod
from Program.Models.AnimalsABS import Animals


class PackAnimalsABS(Animals):
    """Абстрактный класс Вьючные животные"""

    @abstractmethod
    def eat(self):
        """Животное умеет есть"""
        pass

    @abstractmethod
    def speak(self):
        """Животное умеет подавать голос"""
        pass
