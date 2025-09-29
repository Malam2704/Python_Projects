class Vehicle():
    def __init__(self, name, year, model):
        self.name = name
        self.year = year
        self.model = model
        self.mileage = 0

    def get_name(self):
        return self.name
    
    def travel(self, miles):
        self.mileage += miles

    def get_mileage(self):
        return self.mileage
    
    def __str__(self):
        return f"THis is a {self.year} {self.name} {self.model}"
    
class Rivian(Vehicle):
    type = "Electric"

    def __init__(self, name, year, model):
        super().__init__(name, year, model)

def main():
    new_vehicle = Vehicle("v",2020, 1)

    new_rivian = Rivian("Rivver",2025,"Peregrine")
    new_rivian.travel(5000)
    print(new_rivian.type[::2])
    print(new_rivian.get_mileage())

if __name__ == "__main__":
    main()
    