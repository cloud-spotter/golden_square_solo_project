# Customer Order Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class CustomerOrder:
    # User-facing properties:
    # menu: dictionary  

    def __init__(self, menu):
        # Parameters - menu: dictionary containing available items with prices
        # Side effects: Sets the menu property of the self object
        pass # No code here yet

    def view_menu(self):
        # Parameters - menu: dictionary
        # Returns: the self menu object
        # Side-effects: None 
        pass # No code here yet
    
    def select_item(self, item):
        # Parameters - item: string representing a single menu item
        # Returns: Nothing
        # Side-effects: Saves the item to the self object (order) 
        pass # No code here yet

    def calculate_total(self, order):
        # Parameters - order: list representing selected items from the menu
        # Returns: A float total of the customer's selected items
        # Side-effects: Throws an exception if no order exists
        pass # No code here yet

    def view_receipt(self):
        # Returns: A string itemising the customer's order, with prices, and amount due (total)
        # Side-effects: Throws an exception if no order exists
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
1. When a new CustomerOrder object is created
#__init__ creates a menu with available items

"""
customer_order = CustomerOrder()
customer_order.view_menu() # -> {Item 1: 4.00, Item 2: 6.50, Item 3: 7.00}


"""
2. Given an item from the menu
#select_item adds this item to the customer's order

"""
customer_order = CustomerOrder()
customer_order.select_item("Item 2")
customer_order.view_receipt() # -> "Amount due: £6.50. Items ordered: Item 2 - 6.50"


"""
3. Given multiple items from the menu
#select_item adds the items to the customer's order

"""
customer_order = CustomerOrder()
customer_order.select_item("Item 2")
customer_order.select_item("Item 1")
customer_order.view_receipt() # -> "Amount due: £10.50. Items ordered: Item 2 - 6.50, Item 1 - 4.00"


"""
4. Given an item not on the menu
#select_item raises an exception and displays an error message 

"""
customer_order = CustomerOrder()
customer_order.select_item("Artichoke omlette") # -> raises an error with message "Item not on menu."


"""
When a customer requests a receipt
#view_receipt displays the customer's order, with prices, and amount due (total)

"""
# This test is covered by tests 2 & 3 #


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._