class CustomerOrder:
    '''A class to represent a customer's order at a food outlet'''

    def __init__(self, menu: dict) -> None:
        self._menu = menu
        self._order = {}

    def view_menu(self):
        return self._menu
    
    def select_item(self, item: str) -> None:
        if item in self._menu:
            self._order[item] = self._menu[item]
        else: 
            raise Exception("Item not on menu.")
        
    def calculate_total(self):
        total = 0.0
        for item, price in self._order.items():
            total += float(price)
        return total

    def view_receipt(self):
        if self._order == {}:
            raise Exception("Error: no order placed.")
        else:
            return f"Amount due: £{self.calculate_total()}. Items ordered: {self._order}"