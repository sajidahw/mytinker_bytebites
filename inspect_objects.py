from models import Customer, FoodItem, Menu, Transaction
# Create instances of each class and print their attributes
# to inspect the objects

# --- FoodItem ---
burger = FoodItem("Spicy Burger", 8.99, "Mains", 4.5)
soda = FoodItem("Large Soda", 2.49, "Drinks", 3.8)
print("FoodItem:", burger.name, burger.price, burger.category, burger.popularity_rating)
print("FoodItem:", soda.name, soda.price, soda.category, soda.popularity_rating)

# --- Menu ---
menu = Menu()
menu.items.append(burger)
menu.items.append(soda)
print("Menu items:", [item.name for item in menu.items])

# --- Transaction ---
order = Transaction()
order.selected_items.append(burger)
order.selected_items.append(soda)
print("Transaction items:", [item.name for item in order.selected_items])

# --- Customer ---
customer = Customer("Ada")
customer.purchase_history.append(order)
print("Customer:", customer.name)
print("Purchase history count:", len(customer.purchase_history))
