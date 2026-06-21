# Four classes are: Customer, FoodItem, Menu and Transaction.
# Customer: represents a user with a name and a history of past transactions.
# FoodItem: a menu item with a name, price, category, and popularity rating.
# Menu: a collection of FoodItems that can be filtered by category.
# Transaction: an order of selected FoodItems that can compute its total cost.


class Customer:
    def __init__(self, name):
        self.name = name                  # str: the customer's name
        self.purchase_history = []        # list[Transaction]: past orders

    def verify_user(self):
        # operation: verification
        # checks that the customer has a name and at least one past transaction
        return bool(self.name) and bool(self.purchase_history)


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name                  # str: item name, e.g. "Spicy Burger"
        self.price = price                # float: cost of the item
        self.category = category          # str: e.g. "Drinks", "Desserts"
        self.popularity_rating = popularity_rating  # float: rating score


class Menu:
    def __init__(self):
        self.items = []                   # list[FoodItem]: all available items

    def filter_by_category(self, cat):
        # operation: filtering
        # returns only the items whose category attribute matches cat
        return [item for item in self.items if item.category == cat]


class Transaction:
    def __init__(self):
        self.selected_items = []          # list[FoodItem]: items in this order

    def compute_total(self):
        # operation: total calculation
        # adds up the price of every item in selected_items and returns the sum
        total = 0
        for item in self.selected_items:
            total += item.price
        return total
        # alternative: return sum(item.price for item in self.selected_items)


# Manual Testing for each scenario below:
# adding items
brisket_sandwich = FoodItem("Brisket Sandwich", 12.99, "Mains", 4.7)
chicken_salad = FoodItem("Chicken Salad", 9.99, "Mains", 4.3)
diet_coke = FoodItem("Diet Coke", 1.99, "Drinks", 4.2)
lemonade = FoodItem("Lemonade", 2.49, "Drinks", 3.0)

# sorting menus
menu = Menu()
menu.items.extend([brisket_sandwich, diet_coke, lemonade])
print("Menu items before sorting:", [item.name for item in menu.items])
menu.items.sort(key=lambda x: x.popularity_rating, reverse=True)
print("Sorted Menu items by popularity:", [item.name for item in menu.items])

# filtering categories
print("Filtered Menu items (Drinks):", [item.name for item in menu.filter_by_category("Drinks")])
print("Filtered Menu items (Mains):", [item.name for item in menu.filter_by_category("Mains")])


# computing an order total
bill = Transaction()
bill.selected_items.extend([brisket_sandwich, lemonade])
print(" Bill for brisket and lemonade: ", bill.compute_total())
