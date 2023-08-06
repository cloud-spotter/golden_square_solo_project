class CustomerOrder:
    '''A class to represent a customer's order at a food outlet'''
    # User-facing properties:
    # menu: dictionary  

    def __init__(self, menu: dict) -> None:
        # Parameters - menu: dictionary containing available items with prices
        # Side effects: Sets the menu property of the self object
        self.menu = menu
        self.order = {}

    def view_menu(self):
        # Returns: the self menu object
        # Side-effects: None 
        return self.menu
    
    def select_item(self, item: str) -> None:
        # Parameters - item: string representing a single menu item
        # Side-effects: Saves the item to the self object (order) 
        if item in self.menu:
            self.order[item] = self.menu[item]
        else: 
            raise Exception("Item not on menu.")
        
    def calculate_total(self):
        # Returns: A float total of the customer's selected items
        # Side-effects: Throws an exception if no order exists
        total = 0.0
        for item, price in self.order.items():
            total += float(price)
        return total

    def view_receipt(self):
        # Returns: A string itemising the customer's order, with prices, and amount due (total)
        # Side-effects: Throws an exception if no order exists
        if self.order == {}:
            raise Exception("Error: no order placed.")
        else:
            return f"Amount due: £{self.calculate_total()}. Items ordered: {self.order}"