class storage_system():
    def __init__(self):
        self.my_items = {}

    def add_item(self, Product, quantity_added=0):
        if(self.my_items[Product.id]):
            self.my_items[Product.id] = self.my_items[Product.id].change_quantity(quantity_added)
        else:
            Product.change_quantity(quantity_added)
            self.my_items[Product.id] = Product

    def display_items(self):
        for i in list(self.my_items):
            print(self.my_items[i])


class Product:
    def __init__(self, id, name, quantity = 0):
        self.id = id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f" ID: {self.id}\n Name: {self.name} \n Quantity: {self.quantity}\n"
    
    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

def main():
    new_product = Product(12345, "Tablets", 55)
    total_storage = storage_system()
    total_storage.add_item(new_product)

if __name__ == "__main__":
    main()