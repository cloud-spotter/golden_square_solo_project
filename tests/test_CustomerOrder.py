import pytest
from lib.CustomerOrder import *

"""
1. When a new CustomerOrder object is created
#__init__ creates a menu with available items

"""
def test_new_menu_initialised_with_new_class_instance():
    customer_order = CustomerOrder({"Item 1": "4.99", "Item 2": "6.49", "Item 3": "7.99"})
    result = customer_order.view_menu() 
    assert result == {"Item 1": "4.99", "Item 2": "6.49", "Item 3": "7.99"}

"""
2. Given an item from the menu
#select_item adds this item to the customer's order

"""
def test_add_item_to_customer_order():
    customer_order = CustomerOrder({"Item 1": "4.99", "Item 2": "6.49", "Item 3": "7.99"})
    customer_order.select_item("Item 2")
    result = customer_order.view_receipt() 
    assert result == "Amount due: £6.49. Items ordered: {'Item 2': '6.49'}"

# This test fails in cases where prices in the menu have a zero in the pence position
# e.g. 6.50 outputs 6.5 via the calculate_total() method which returns a float
# Ran out of time to fix this within the weekend challenge window though

"""
3. Given multiple items from the menu
#select_item adds the items to the customer's order

"""
def test_add_multiple_items_to_customer_order():
    customer_order = CustomerOrder({"Item 1": "4.99", "Item 2": "6.49", "Item 3": "7.99"})
    customer_order.select_item("Item 2")
    customer_order.select_item("Item 1")
    result = customer_order.view_receipt()
    assert result == "Amount due: £11.48. Items ordered: {'Item 2': '6.49', 'Item 1': '4.99'}"

"""
4. Given an item not on the menu
#select_item raises an exception and displays an error message 

"""
def test_add_item_not_on_menu_raises_error():
    customer_order = CustomerOrder({"Item 1": "4.99", "Item 2": "6.49", "Item 3": "7.99"})
    with pytest.raises(Exception) as e:
        customer_order.select_item("Artichoke omlette")
    error_message = str(e.value)
    assert error_message == "Item not on menu."


"""
5. When a customer requests a receipt for an empty order
#view_receipt raises an exception and displays an error message

"""
def test_view_receipt_raises_error_for_empty_order():
    customer_order = CustomerOrder({"Item 1": "4.99", "Item 2": "6.49", "Item 3": "7.99"})
    with pytest.raises(Exception) as e:
        customer_order.view_receipt()
    error_message = str(e.value)
    assert error_message == "Error: no order placed."