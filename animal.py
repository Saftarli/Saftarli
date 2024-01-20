# Animal sinfinin təyin olunması

class Animal:
    # __init__ metodu obyektin yaradılması üçün çağırılır

    def __init__(self,name, species):
        self.name = name
        self.species = species

    # Səs metodu - Polimorfizm nümunəsi
    def make_sound(self):
        pass # Alt siniflər bu metodunu özəlləşdirəcəklər


class Dog(Animal):
# __init__ metodu təyin olunacaq, əgər istifadəçi adını vermişlərsə, "Unknown" olaraq qeyd edilir
    def __init__(self, name="Unknown", breed="Unknown", color="Unknown"):
        super().__init__(name, species=Dog)
        self.breed = breed
        self.name = name
        self.color = color

    def make_sound(self):
        return "Woof!"
    
# Cat sinifi Animal sinifi üzərindən irəliləyən sinifdir
class Cat(Animal):
    def __init__(self, name="Unknown", breed="Unknown", color="Unknown"):
        super().__init__(name, species=Cat)
        self.breed = breed
        self.name = name
        self.color = color


    def make_sound(self):
        return "Meow!"

# Animal sinifindən obyektlərin yaradılması
    
animal = Animal(name="Generic Animal", species="Unknown")
dog = Dog(name="Buddy", breed="Golden Retriever", color="Golden")
cat = Cat(name="Garfield", breed="street cat", color="Yellow")

# Obyektin xwsusiyyətlərinin və metodlarının çağırılması

print(f"{animal.name} is an {animal.species}")
print(f"{dog.name} is a {dog.breed} {dog.species} {dog.color}")
print(f"{cat.name} is a {cat.breed} {cat.species} {cat.color}")

# Polimorfizm - hər iki obyektin də eyni metodunun çağırılması
print(animal.make_sound()) # Çıxış gözlənilmir, çünki make_sound metodu Animal sinifində pass ilə təyin olunub
print(dog.make_sound()) # Çıxış : Woof!
print(cat.make_sound()) # Çıxış : Meow!