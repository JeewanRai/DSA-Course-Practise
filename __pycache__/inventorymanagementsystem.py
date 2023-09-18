class Product:
    """
    Represents a product with its attributes.

    Attributes:
        - product_name (str): The name of the product.
        - product_price (float): The price of the product.
    """

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def __str__(self):
        return f"{self.product_name} -Nu.{self.product_price:.2f}"


class Storage:
    """
    Represents a storage facility where products are stored.

    Attributes:
        - storage_name (str): The name of the storage facility.
        - stored_products (list of Product): List of products in the storage facility.
    """

    def __init__(self, storage_name):
        self.storage_name = storage_name
        self.stored_products = []

    def add_product(self, product):
        """Add a product to the storage facility."""
        self.stored_products.append(product)

    def list_products(self):
        """List all products in the storage facility."""
        return self.stored_products

    def __str__(self):
        return f"Storage Facility: {self.storage_name}"


class CargoShipment:
    """
    Represents a shipment of products from one storage facility to another.

    Attributes:
        - source_storage (Storage): The source storage facility.
        - destination_storage (Storage): The destination storage facility.
        - cargo (list of Product): List of products in the shipment.
    """

    def __init__(self, source_storage, destination_storage):
        self.source_storage = source_storage
        self.destination_storage = destination_storage
        self.cargo = []

    def add_product(self, product):
        """Add a product to the cargo shipment."""
        self.cargo.append(product)

    def ship_cargo(self):
        """Ship the products from the source storage facility to the destination storage facility."""
        for product in self.cargo:
            self.source_storage.stored_products.remove(product)
            self.destination_storage.add_product(product)

    def __str__(self):
        return f"Cargo Shipment from {self.source_storage.storage_name} to {self.destination_storage.storage_name}"


# Example usage with different names:

# Create products
product1 = Product("Laptop", 999.99)
product2 = Product("Smartphone", 499.99)
product3 = Product("Tablet", 299.99)

# Create storage facilities
storage1 = Storage("Storage A")
storage2 = Storage("Storage B")

# Add products to storage facilities
storage1.add_product(product1)
storage1.add_product(product2)
storage2.add_product(product3)

# Create a cargo shipment from Storage A to Storage B
cargo_shipment = CargoShipment(storage1, storage2)
cargo_shipment.add_product(product1)
cargo_shipment.add_product(product3)

# List products in Storage A before shipment
print(f"Products in {storage1.storage_name} before shipment:")
for product in storage1.list_products():
    print(product)

# List products in Storage B before shipment
print(f"Products in {storage2.storage_name} before shipment:")
for product in storage2.list_products():
    print(product)

# Ship the cargo
cargo_shipment.ship_cargo()

# List products in Storage A after shipment
print(f"Products in {storage1.storage_name} after shipment:")
for product in storage1.list_products():
    print(product)

# List products in Storage B after shipment
print(f"Products in {storage2.storage_name} after shipment:")
for product in storage2.list_products():
    print(product)
