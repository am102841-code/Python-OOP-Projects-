class Inventory:
    def __init__(self):
        self.capacity = 10
        self.items = []
        self.item_count = 0

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Added {item} to inventory.")
        else:
            print("Inventory is full.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from inventory.")
        else:
            print(f"{item} is not in inventory.")

    def display_inventory(self):
        print("Inventory:")
        for item in self.items:
            print(f"- {item}")
        print(f"Capacity: {len(self.items)}/{self.capacity}")

    def check_item(self, item):
        if item in self.items:
            print(f"{item} is in inventory.")
        else:
            print(f"{item} is not in inventory.")

    def clear_inventory(self):
        self.items = []

    def count_items(self):
        items_count = 0
        for x in self.items:
            items_count += 1
        return items_count

inventory = Inventory() # Create an instance of Inventory
inventory.add_item("Sword")
inventory.add_item("Health Potion")
inventory.add_item("Shield")
inventory.display_inventory()
inventory.check_item("Sword")
inventory.remove_item("Shield")
inventory.display_inventory()
inventory.clear_inventory()
inventory.display_inventory()
