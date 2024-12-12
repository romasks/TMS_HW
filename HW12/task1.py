from dataclasses import dataclass, field
from pprint import pprint
from multipledispatch import dispatch
from operator import attrgetter

@dataclass
class Product:
    name: str
    shop: str
    cost: float

class Warehouse:
    def __init__(self) -> None:
        self.products = list()

    def put_product(self, product):
        self.products.append(product)

    @dispatch(int)
    def show_product(self, index) -> None:
        if index not in range(0, len(self.products)):
            print("Index out of range")
            return
        print(self.products[index])
    
    @dispatch(str)
    def show_product(self, name) -> None:
        for product in self.products:
            if product.name == name:
                print(product)
                return
        print("No such product")

    def show_products(self) -> None:
        pprint(self.products)

    def sort_by_field(self, field_name) -> None:
        self.products = sorted(self.products, key = attrgetter(field_name))


product_1 = Product("p1", "s1", 123)
product_2 = Product("p2", "s1", 23)
product_3 = Product("p3", "s1", 456)
product_4 = Product("p4", "s1", 87)

warehouse = Warehouse()
warehouse.put_product(product_1)
warehouse.put_product(product_2)
warehouse.put_product(product_3)
warehouse.put_product(product_4)
warehouse.show_products()
print()

warehouse.show_product(1)
warehouse.show_product("p1")
print()

warehouse.sort_by_field("cost")
warehouse.show_products()
print()

warehouse.sort_by_field("name")
warehouse.show_products()
print()
