#Object Oriented Programmin - OOP

#Objects and #Classes

#Attributes - Xüsusiyyətlər , Markası, Model, Rəngi
#Methods - Start, Stop

#İnheritance - Miras
#Polimorphism - Polimorfizm
#Special Methods - Xüsusi metodlar __init__

# Sinifin təyin olunması

class Car:
    # __init__ metodu obyektin yaradılması zamanı çağırılır
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    # Bir metod necə təyin olunur
    def start(self):
        print(f"{self.brand} {self.model} {self.color} car started.")

    # Başqa bir metodun əlavə olunması
    def stop(self):
        print(f"{self.brand} {self.model} {self.color} car stopped.")

# Obyektin yaradılması
my_car = Car(brand="Toyota", model="Corolla", color="Gray")

# Obyektin metodlarının çağırılması
my_car.start()
my_car.stop()






