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
        # return True if self.name is a non-empty string
        pass


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
        # return list of items whose category matches cat
        pass


class Transaction:
    def __init__(self):
        self.selected_items = []          # list[FoodItem]: items in this order

    def compute_total(self):
        # return sum of price for each item in selected_items
        pass
