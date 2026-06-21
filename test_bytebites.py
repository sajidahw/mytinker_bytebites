# run: pytest test_bytebites.py -v
import pytest
from models import Customer, FoodItem, Menu, Transaction


# --- Logic Tests ---

def test_calculate_total_with_multiple_items():
    # verify that a $10 burger + $5 soda totals $15
    burger = FoodItem("Burger", 10.00, "Mains", 4.0)
    soda = FoodItem("Soda", 5.00, "Drinks", 3.5)
    order = Transaction()
    order.selected_items.extend([burger, soda])
    assert order.compute_total() == pytest.approx(15.0)  # approx() checks within a small tolerance to handle float precision


def test_filter_returns_only_matching_category():
    # verify filtering "Drinks" returns only drink items, not mains
    burger = FoodItem("Burger", 10.00, "Mains", 4.0)
    soda = FoodItem("Soda", 5.00, "Drinks", 3.5)
    water = FoodItem("Water", 1.00, "Drinks", 4.0)
    menu = Menu()
    menu.items.extend([burger, soda, water])
    result = menu.filter_by_category("Drinks")
    assert result == [soda, water]


def test_filter_returns_empty_list_for_unknown_category():
    # verify filtering a non-existent category returns [], not an error
    burger = FoodItem("Burger", 10.00, "Mains", 4.0)
    menu = Menu()
    menu.items.append(burger)
    assert menu.filter_by_category("Desserts") == []


def test_verify_user_returns_true_for_valid_customer():
    # verify a customer with a name and purchase history is confirmed real
    customer = Customer("Ada")
    customer.purchase_history.append(Transaction())
    assert customer.verify_user() is True


def test_verify_user_returns_false_with_no_history():
    # verify a new customer with no purchases is not yet verified
    customer = Customer("Ada")
    assert customer.verify_user() is False


# --- Edge Case Tests ---

def test_order_total_is_zero_when_empty():
    # verify an empty transaction returns $0 and does not crash
    order = Transaction()
    assert order.compute_total() == 0.0


def test_filter_on_empty_menu_returns_empty_list():
    # verify filtering an empty menu returns [] and does not crash
    menu = Menu()
    assert menu.filter_by_category("Drinks") == []


def test_verify_user_returns_false_for_empty_name():
    # verify a customer with an empty name string is not verified
    customer = Customer("")
    customer.purchase_history.append(Transaction())
    assert customer.verify_user() is False


# --- Run all tests ---
# if __name__ == "__main__":
#     test_calculate_total_with_multiple_items()
#     test_filter_returns_only_matching_category()
#     test_filter_returns_empty_list_for_unknown_category()
#     test_verify_user_returns_true_for_valid_customer()
#     test_verify_user_returns_false_with_no_history()
#     test_order_total_is_zero_when_empty()
#     test_filter_on_empty_menu_returns_empty_list()
#     test_verify_user_returns_false_for_empty_name()
#     print("All tests passed.")
