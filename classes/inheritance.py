from dataclasses import dataclass


class Mapping:
    __user_id = "300"

    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def __add(self, item):
        """private function"""
        self.items_list.append(item)

    def update(self, iterable):
        for item in iterable:
            self.__add(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


mapping = Mapping([1, 2, 3])
mapping.update([4, 5])
print(mapping.items_list)

sub_mapping = MappingSubclass([])
sub_mapping.update((1, 2), (3, 4))
print(sub_mapping.items_list)


@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
print(john)


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    __total = 10

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


inv_item = InventoryItem('Bob', 34.67, 2)
print(inv_item.__str__())
print(str(inv_item))
print(repr(inv_item))
print(inv_item.total_cost())
inv_item.__setattr__('quantity_on_hand', 3)
print(inv_item.total_cost())
print(inv_item.__getattribute__('quantity_on_hand'))
print(inv_item.__getstate__())
