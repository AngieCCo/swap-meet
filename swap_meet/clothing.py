from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, age=0, id=None, fabric="Unknown", condition=0):
        super().__init__(age, id, condition)
        self.fabric = fabric
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."