class Animal:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name  # Public method to access private attribute

    def set_name(self, name):
        self.__name = name  # Public method to modify private attribute


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.get_name()} says Woof!")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        print(f"{self.get_name()} says Meow!")


puppy = Dog("Buddy", "Golden Retriever")
puppy.bark()  # Output: Buddy says Woof!

cat = Cat("Whiskers", "Tabby")
cat.meow()  # Output: Whiskers says Meow!
