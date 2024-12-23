# Vehicle Class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print(f"{self.model} is moving along..")

    def get_make_model(self):
        return f"I'm a {self.make} {self.model}."

# Airplane Class
class Airplane(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def moves(self):
        print(f"Flies Along..")

# Truck Class
class Truck(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def moves(self):
        print(f"Rumbles Along..")

# GolfCart Class
class GolfCart(Vehicle):
    pass

# Objects
# Vehicle object
my_car = Vehicle("Ford", "Mustang")
print(my_car.make)
print(my_car.model)
my_car.moves()
print(my_car.get_make_model())

# Airplane Object
cessna = Airplane("Cessna", "SkyHawk")
cessna.moves()
print(cessna.get_make_model())

# Truck Object
mack = Truck("Mack", "Pinnacle")
mack.moves()
print(mack.get_make_model())

# GolfCart Object
golfwagon = GolfCart("Yamaha", "GC100")
golfwagon.moves()
print(golfwagon.get_make_model())

print("\n\n")

for v in (my_car, cessna, mack, golfwagon):
    print(v.get_make_model())
    v.moves()
