from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass

class Cat(Animal):
    def say(self):
        return "Meow!"

class Dog(Animal):
    def say(self):
        return "Woof!"
