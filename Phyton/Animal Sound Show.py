from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def __init__(self, name, habit):
        self.name = name
        self.habit = habit
    def display(self):
        print(f"Name: {self.name}")
        print(f"Habit: {self.habit}")
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
        def __init__(self, name, habit, breed):
            super().__init__(name, habit)
            self.breed = breed
        def make_sound(self):
            print(f"{self.name} {self.breed} says: Woof! Woof!")
class Parrot(Animal):
        def __init__(self, name, habit, phrase):
            super().__init__(name, habit)
            self.phrase = phrase
        def make_sound(self):
            print(f"{self.name} says: {self.phrase}!")
class Lion(Animal):
                def __init__(self, name, habit, pride):
                    super().__init__(name, habit)
                    self.pride = pride
                def make_sound(self):
                    print(f"{self.name} (Pride: {self.pride}) says: Roar! Roar!")
my_dog = Dog("Bruno", "Home", "Labrador")
my_parrot = Parrot("Polly", "Jungle", "Squawk!")
my_lion = Lion("Simba", "Savannah", "Pride Rock")


my_dog.display()
my_dog.make_sound()

my_parrot.display()
my_parrot.make_sound()

my_lion.display()
my_lion.make_sound()
