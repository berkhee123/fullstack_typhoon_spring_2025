# Animal nertei klass uusgeerei. name gedeg class attribute-tai baina.
# speak gedeg funktstei baina. enehuu funts ni yu ch hiihgui bogood uuniig pass
# gej temdegleerei
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

# Dinosaur gedeg animal obiykt uusgene uu 
dinosaur = Animal("Dinosaur")
print(dinosaur.name) # Dinosaur
dinosaur.speak() # ? 

# Problems: Dog, Cat gedeg animal toroltoi klassuudiig uusgue. Tuhain klass bolgoniig 
# oorsdiinh ni dugaar hariuldag bolgooroi 
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# cat gedeg klassiig Meow gedeg bolgono uu

# 1 muur, 1 nohoi object-uudiig uusgeed tuuniigee speak hiilgene uu.
fido = Dog("Fido")
whiskers = Cat("whiskers")

print(fido.speak()) # Fido says Woof!
print(whiskers.speak()) # Whiskers says Meow!

# Human gedeg klass uusgeed tuundee humuusiig boddog bolgono uu
# enehuu funkts ni zaaval implement hiisgdsen baih shaardlagagui 
# odoo tuunees Mongolian, Chinese gesen 2 torliin race uusgene uu
# tegeed yridag bolgohdoo tuhain heleer n' mendchildeg bolgooroi 

class Human:
    def __init__(self,name):
        self.name = name
    
    def think(self):
        pass

    def talk(self):
        pass


class Mongolian(Human):
    def talk(self):
        return f"{self.name} speaks: Sain baina uu!"
    def think(self):
        return f"Mongolian {self.name} is thinking"

class Chinese(Human):
    def talk(self):
        return f"{self.name} speaks: Ni hao ma!" 
    
    def think(self):
        return f"Chinese Man {self.name} is thinking"

berkh = Mongolian("Berkhee")
huang = Chinese("wang")
print(berkh.talk())




