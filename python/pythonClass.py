# define a generic Vehicle CLASS
class Vehicle():
    # constructor
    def __init__(self, vin, make,model):
        self.vin = vin
        self.make = make
        self.model = model
        self.running = False
    def start(self):
        self.running = True
    def stop(self):
        self.running = False
    def __str__(self):
        return f"Vehicle ({self.vin}) is a {self.make} model {self.model}"


car = Vehicle('TS123', 'Tesla', 'Model S')
print(car.running) # -> False
car.start()
print(car.running) # -> True
plane = Vehicle('X99Y', 'Boeing', '747-B')
print(plane.vin, plane.make, plane.model)
print(car)
