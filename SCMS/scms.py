total_storage = {}

def print_storage():
    for i in list(total_storage):
        print(total_storage[i])

class Product:
    def __init__(self, id, name, quantity = 0):
        self.id = id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f" ID: {self.id}\n Name: {self.name} \n Quantity: {self.quantity}\n"

def main():
    new_product = Product(12345, "Tablets", 55)
    total_storage[new_product.id] = new_product

    print_storage()

if __name__ == "__main__":
    main()