class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        print(self.name + ": Meow!")

    def purr(self):
        print(self.name + ": Purr...")

    def eat(self):
        print(self.name + ": cccc...")

cat1 = Cat("leo", "black", 5)
print(cat1.name)
print(cat1.color)
print(cat1.age)
cat1.meow()
cat1.purr()
cat1.eat()
