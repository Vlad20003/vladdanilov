import doctest
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int):
        Vehicle("Toyota", "Camry", 2020)
        if not isinstance(make, str):
            raise TypeError("Производитель должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(year, int) or year <= 1885:
            raise ValueError("Год выпуска должен быть целым числом больше 1885")

        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        vehicle = Vehicle("Toyota", "Camry", 2020)
        vehicle.start_engine()

    @abstractmethod
    def stop_engine(self) -> None:
        vehicle = Vehicle("Toyota", "Camry", 2020)
        vehicle.stop_engine()


class VideoGame(ABC):
    def __init__(self, title: str, genre: str, release_year: int):
        VideoGame("The Last of Us", "Action-adventure", 2013)

        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(genre, str):
            raise TypeError("Жанр должен быть строкой")
        if not isinstance(release_year, int) or release_year < 1950:
            raise ValueError("Год выпуска должен быть целым числом не менее 1950")

        self.title = title
        self.genre = genre
        self.release_year = release_year

    @abstractmethod
    def start_game(self) -> None:
        game = VideoGame("The Last of Us", "Action-adventure", 2013)
        game.start_game()

    @abstractmethod
    def save_game(self) -> None:
        game = VideoGame("The Last of Us", "Action-adventure", 2013)
        game.save_game()


class Queue(ABC):
    def __init__(self, max_size: int):
        Queue(5)

        if not isinstance(max_size, int) or max_size <= 0:
            raise ValueError("Максимальный размер очереди должен быть целым положительным числом")

        self.max_size = max_size
        self.queue = []

    @abstractmethod
    def enqueue(self) -> None:
        queue = Queue(3)
        queue.enqueue()

    @abstractmethod
    def dequeue(self) -> None:
        queue = Queue(3)
        queue.dequeue()


if __name__ == "__main__":
    doctest.testmod()
    pass
