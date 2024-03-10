from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def saisir(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass

    @abstractmethod
    def affichage(self):
        pass
