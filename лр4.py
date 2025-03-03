class Automobile:
    """Базовый класс для автомобилей."""

    def __init__(self, brand: str, model: str, year: int):
        """Инициализация атрибутов автомобиля.

        Args:
            brand: Бренд автомобиля.
            model: Модель автомобиля.
            year: Год выпуска.
        """
        self.__brand = brand  # Сделан непубличным для инкапсуляции
        self.__model = model  # Сделан непубличным для инкапсуляции
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"{self.year} {self.__brand} {self.__model}"

    def __repr__(self) -> str:
        """Возвращает официальный строковый представление автомобиля."""
        return f"Automobile(brand='{self.__brand}', model='{self.__model}', year={self.year})"

    def start_engine(self) -> None:
        """Запускает двигатель автомобиля."""
        print(f"The engine of {self} is running.")


class PassengerCar(Automobile):
    """Класс легкового автомобиля, наследующий от Automobile."""

    def __init__(self, brand: str, model: str, year: int, doors: int):
        """Инициализация легкового автомобиля.

        Args:
            brand: Бренд автомобиля.
            model: Модель автомобиля.
            year: Год выпуска.
            doors: Количество дверей.
        """
        super().__init__(brand, model, year)
        self.doors = doors

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} with {self.doors} doors"

    def start_engine(self) -> None:
        """Запускает двигатель легкового автомобиля.

        Переопределяет родительский метод для добавления текста о легковом автомобиле.
        """
        print(f"The engine of the passenger car {self} is purring.")


if __name__ == "__main__":
    # Пример использования классов
    car1 = PassengerCar("Toyota", "Camry", 2021, 4)
    print(car1)  # Вывод: 2021 Toyota Camry with 4 doors
    print(repr(car1))  # Вывод: Automobile(brand='Toyota', model='Camry', year=2021)
    car1.start_engine()  # Вывод: The engine of the passenger car 2021 Toyota Camry with 4 doors is purring.
