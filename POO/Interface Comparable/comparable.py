from abc import ABC, abstractmethod

class Comparable(ABC) :

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def compareTo(obj1,obj2) :
        pass