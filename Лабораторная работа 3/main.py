# TODO Написать 3 класса с документацией и аннотацией типов

class AbstractObject:
    def init(self, name: str, color: str):

        """
    Constructor for AbstractObject class.

    python
    Copy code
        :param name: A string representing the name of the object.
        :param color: A string representing the color of the object.
        """


self.name = name
self.color = color

def move(self, direction: str):
    """
    Move the object in a specified direction.

    :param direction: A string representing the direction to move the object.
    :return: A message confirming the movement of the object.

    >>> obj = AbstractObject("obj1", "red")
    >>> obj.move("up")
    'Object obj1 moved up.'
    """

def change_color(self, new_color: str):
    """
    Change the color of the object.

    :param new_color: A string representing the new color of the object.
    :return: A message confirming the color change.

    >>> obj = AbstractObject("obj2", "blue")
    >>> obj.change_color("green")
    'Object obj2 color changed to green.'
    """


def interact(self):
    """
    Perform an interaction with the object.

    :return: A message describing the interaction.

    >>> obj = AbstractObject("obj3", "yellow")
    >>> obj.interact()
    'Object obj3 interacted with.'
    """

    class Tree(AbstractObject):
        def init(self, name: str, color: str, age: int):

            """
        Constructor for Tree class.

        python
        Copy code
            :param name: A string representing the name of the tree.
            :param color: A string representing the color of the tree.
            :param age: An integer representing the age of the tree.
            """

    super().__init__(name, color)
    self.age = age


def grow(self, years: int):
    """
    Simulate the growth of the tree over a specified number of years.

    :param years: An integer representing the number of years for the tree to grow.
    :return: A message indicating the growth of the tree.

    >>> tree = Tree("oak", "green", 10)
    >>> tree.grow(5)
    'Tree oak grew 5 years.'
    """


class Car(AbstractObject):
    def init(self, name: str, color: str, brand: str):

        """
    Constructor for Car class.

    python
    Copy code
        :param name: A string representing the name of the car.
        :param color: A string representing the color of the car.
        :param brand: A string representing the brand of the car.
        """


super().__init__(name, color)
self.brand = brand


def drive(self, distance: float):
    """
    Simulate driving the car for a specified distance.

    :param distance: A float representing the distance in kilometers to drive.
    :return: A message indicating the distance driven.

    >>> car = Car("sedan", "silver", "Toyota")
    >>> car.drive(50.5)
    'Car sedan driven 50.5 km.'
    """


def honk(self):
    """
    Produce a honking sound from the car horn.

    :return: A message indicating the car horn has honked.

    >>> car = Car("SUV", "black", "Ford")
    >>> car.honk()
    'Car SUV horn honked.'
    """