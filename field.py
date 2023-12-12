ANIMALS = {"s": "sloth", "d": "doggo", "@": "cat", "m": "moogle", "c": "chocobo"}


def explore_tile(char, row, col):
    """
    Explore a tile - if there is an animal, prints the
    location and name of the animal"""
    animal = ANIMALS.get(char)
    if animal:
        print(f"Tile ({col}, {row}) contains {animal}")
    # elif animal != " ":
    # print(f"Tile ({col}, {row}) contains {char}")


def explore_field(listi):
    """
    This function explores an entire field by calling the explore_tile
    function for each tile in the field."""
    for n_row, row in enumerate(field):
        for n_col, i in enumerate(row):
            explore_tile(listi[n_row][n_col], n_row, n_col)


field = [
    [" ", "s", " ", " ", "m"],
    [" ", "d", "@", "d", " "],
    ["c", " ", "s", "d", " "],
]
explore_field(field)
