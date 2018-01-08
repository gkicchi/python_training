class Dog:
    name = ""
    def bark(self):
        m = self.name + ": Bow-wow!"
        print m

pochi1 = Dog()
pochi1.name = "Pochi"
pochi1.bark()

hachi1 = Dog()
hachi1.name = "Hachi"
hachi1.bark()

pochi1.bark()
