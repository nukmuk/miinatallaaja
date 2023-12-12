def select_quantity(item):
    return item[1]


inventory = [("donkey", 12), ("Moomin mug", 1), ("poleax", 4)]
inventory.sort(None, select_quantity())
print(inventory)
